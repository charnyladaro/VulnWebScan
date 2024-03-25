def generate_report(vulnerabilities):
    if not vulnerabilities:
        print("No vulnerabilities detected.")
        return

    print("Vulnerabilities detected:")
    for vulnerability in vulnerabilities:
        print(
            f"URL: {vulnerability['url']}, Vulnerability: {vulnerability['vulnerability']}"
        )
