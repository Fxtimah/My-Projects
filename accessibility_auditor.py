"""
Accessibility Website Auditor
Author: Fatimah Agboola

A Python accessibility auditing tool that scans a webpage for basic accessibility issues.
Skills demonstrated:
- Web scraping
- Accessibility awareness
- HTML parsing
- Automated reporting
- Error handling

Checks include:
- Images missing alt text
- Pages missing title
- Heading structure
- Links without readable text
- Form inputs missing labels
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class AccessibilityAuditor:
    def __init__(self, url: str):
        self.url = self.validate_url(url)
        self.soup = None
        self.issues = []

    @staticmethod
    def validate_url(url: str) -> str:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError("Invalid URL provided.")

        return url

    def fetch_page(self) -> None:
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as error:
            raise ConnectionError(f"Could not fetch website: {error}")

    def check_page_title(self) -> None:
        title = self.soup.find("title")
        if not title or not title.get_text(strip=True):
            self.issues.append("Missing or empty page title.")

    def check_images_alt_text(self) -> None:
        images = self.soup.find_all("img")
        missing_alt = [
            image for image in images
            if not image.has_attr("alt") or not image.get("alt", "").strip()
        ]

        if missing_alt:
            self.issues.append(f"{len(missing_alt)} image(s) missing alt text.")

    def check_heading_structure(self) -> None:
        headings = self.soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        if not headings:
            self.issues.append("No headings found. Headings help structure content for screen readers.")
            return

        h1_count = len(self.soup.find_all("h1"))

        if h1_count == 0:
            self.issues.append("No H1 heading found.")
        elif h1_count > 1:
            self.issues.append(f"Multiple H1 headings found ({h1_count}). Consider using one main H1.")

    def check_links_text(self) -> None:
        links = self.soup.find_all("a")
        empty_links = [
            link for link in links
            if not link.get_text(strip=True) and not link.get("aria-label")
        ]

        if empty_links:
            self.issues.append(f"{len(empty_links)} link(s) missing readable text or aria-label.")

    def check_form_labels(self) -> None:
        inputs = self.soup.find_all("input")
        labels = self.soup.find_all("label")

        label_for_values = {
            label.get("for")
            for label in labels
            if label.get("for")
        }

        unlabeled_inputs = []
        for input_field in inputs:
            input_type = input_field.get("type", "").lower()
            input_id = input_field.get("id")

            if input_type in ["hidden", "submit", "button"]:
                continue

            has_label = input_id in label_for_values if input_id else False
            has_aria = input_field.get("aria-label") or input_field.get("aria-labelledby")

            if not has_label and not has_aria:
                unlabeled_inputs.append(input_field)

        if unlabeled_inputs:
            self.issues.append(f"{len(unlabeled_inputs)} form input(s) missing labels or ARIA attributes.")

    def run_audit(self) -> None:
        self.fetch_page()
        self.check_page_title()
        self.check_images_alt_text()
        self.check_heading_structure()
        self.check_links_text()
        self.check_form_labels()

    def generate_report(self) -> None:
        print("\nAccessibility Audit Report")
        print("=" * 50)
        print(f"Website: {self.url}")
        print("-" * 50)

        if not self.issues:
            print("No major accessibility issues found from basic checks.")
        else:
            for index, issue in enumerate(self.issues, start=1):
                print(f"{index}. {issue}")

        print("-" * 50)
        print("Note: This is a basic automated audit. Manual testing is still recommended.")


def main() -> None:
    print("Accessibility Website Auditor")
    url = input("Enter website URL: ").strip()

    try:
        auditor = AccessibilityAuditor(url)
        auditor.run_audit()
        auditor.generate_report()
    except (ValueError, ConnectionError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
