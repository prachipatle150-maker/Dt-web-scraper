DT Web Scraper – Task 1
Overview
This is a simple web scraper I built as part of the DeepThought (DT) assignment.
It takes a company website URL and extracts structured information about the company in a clean, organized way.

The scraper focuses on:
Extracting information accurately (without guessing)
Creating structured JSON output
Handling missing pages or JavaScript-heavy websites

Tech Stack
Python
requests
BeautifulSoup
json
datetime

How It Works
The script takes a single input:
Company website URL
It tries to visit a few important pages (maximum 10–15), such as:

Home
/about
/products
/solutions
/contact
/careers
Only publicly accessible pages are processed.

Output
The scraper produces a JSON file containing:
Company details
Business summary (basic overview)
Pages found
Any evidence or signals detected
Contact and hiring information
Metadata (timestamp, visited pages, errors)
If any information is missing, it is clearly marked as "Not found".

How to Run
Install required dependencies.
Run scraper.py.
Enter a company website URL when prompted.
JSON output will be saved in the outputs/ folder.
Demo Runs
I tested the scraper on the following websites:
Nestlé Health Science
Himalaya Wellness
JSON outputs for these runs are available in the outputs/ folder.

Notes
Some websites rely heavily on JavaScript, so not all content can be fetched directly.
The scraper is designed to be honest: it logs when information cannot be found instead of making guesses.
This project is meant to be a lightweight, reliable tool for structured data extraction—not a full-scale web crawler.
The goal was to build something practical and easy to understand, so it can be extended for other websites in the future.
