import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def crawl_website(url):
    crawled_urls = set()
    queue = [url]

    while queue:
        current_url = queue.pop(0)

        # Fetch the HTML content of the current URL
        try:
            response = requests.get(current_url)
            response.raise_for_status()  # Raise an exception for any HTTP errors
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL '{current_url}': {e}")
            continue

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract all links (href attributes) from the current page
        links = soup.find_all("a", href=True)
        for link in links:
            absolute_url = urljoin(current_url, link["href"])
            if absolute_url.startswith(url):
                if absolute_url not in crawled_urls:
                    crawled_urls.add(absolute_url)
                    queue.append(absolute_url)

    return crawled_urls


def save_crawled_urls(crawled_urls, folder_path):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "crawled_urls.txt")
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        for url in crawled_urls:
            file.write(url + "\n")
        file.write("\n")
        file.write("=" * 100 + "\n")
        file.write("\n")


# Example usage:
if __name__ == "__main__":
    target_url = input("Enter the URL of the target web application: ").strip()
    crawled_urls = crawl_website(target_url)
    save_crawled_urls(crawled_urls, "VulnWebScan/crawled")
    print("Crawled URLs saved successfully.")
