import argparse
from modules.crawler import crawl_website, save_crawled_urls
from modules.vulnerability_detection import detect_vulnerabilities
from modules.reporting import generate_report


def get_target_url():
    # Prompt the user to enter the URL of the target web application
    target_url = input("Enter the URL of the target web application: ").strip()
    return target_url


def main():
    # Get the URL of the target web application from the user
    target_url = get_target_url()

    # Step 1: Crawl the target website
    print("Crawling the target website...")
    crawled_urls = crawl_website(target_url)
    print(f"Found {len(crawled_urls)} URLs.")

    # Step 2: Save crawled URLs
    save_crawled_urls(crawled_urls, "VulnWebScan/crawled")

    # Step 2: Detect vulnerabilities
    print("Detecting vulnerabilities...")
    vulnerabilities = detect_vulnerabilities(crawled_urls)
    print(f"Found {len(vulnerabilities)} vulnerabilities.")

    # Step 3: Generate vulnerability report
    print("Generating vulnerability report...")
    generate_report(vulnerabilities)

    print("VulnWebScan completed successfully.")


if __name__ == "__main__":
    main()
