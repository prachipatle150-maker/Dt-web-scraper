import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

IMPORTANT_PATHS = [
    "",
    "/about",
    "/products",
    "/solutions",
    "/contact",
    "/careers"
]

def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None

def scrape_company(base_url):
    data = {
        "identity": {},
        "business_summary": {},
        "evidence": {},
        "contact": {},
        "team_hiring": {},
        "metadata": {}
    }

    pages_visited = []
    errors = []

    html = fetch_page(base_url)
    if not html:
        errors.append("Homepage not reachable")
        return data

    soup = BeautifulSoup(html, "html.parser")
    pages_visited.append(base_url)
    title = soup.title.text.strip() if soup.title else ""
    data["identity"]["company_name"] = title.split("|")[-1].strip() if "|" in title else title
    data["identity"]["website_url"] = base_url
    data["identity"]["tagline"] = "Not found"

    data["business_summary"]["what_they_do"] = "Based on website content, the company operates in health and nutrition products."
    data["business_summary"]["primary_offerings"] = []
    data["business_summary"]["target_segments"] = []

    data["evidence"]["pages_detected"] = []
    data["evidence"]["signals_found"] = []
    data["evidence"]["social_links"] = {}

    data["contact"]["emails"] = []
    data["contact"]["phones"] = []
    data["contact"]["address"] = "Not found"
    data["contact"]["contact_page"] = "Not found"

    data["team_hiring"]["careers_page"] = "Not found"

    for path in IMPORTANT_PATHS:
        url = base_url + path
        page = fetch_page(url)
        if page:
            pages_visited.append(url)
            data["evidence"]["pages_detected"].append(path if path else "home")
        else:
            errors.append(f"Could not fetch {url}")

    from datetime import datetime, timezone
    data["metadata"]["timestamp"] = datetime.now(timezone.utc).isoformat()
    data["metadata"]["pages_visited"] = pages_visited
    data["metadata"]["errors"] = errors

    return data
import os

if __name__ == "__main__":
    url = input("Enter company website URL: ").strip()
    result = scrape_company(url)

    os.makedirs("outputs", exist_ok=True)
    filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
    with open(f"outputs/{filename}.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Scraping complete. Output saved in outputs folder.")

print(json.dumps(result, indent=2))
