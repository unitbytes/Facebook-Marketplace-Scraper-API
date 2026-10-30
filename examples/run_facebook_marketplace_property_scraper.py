#!/usr/bin/env python3
"""
Facebook Marketplace Property & Rentals Scraper — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/facebook-marketplace-property-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/facebook-marketplace-property-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_facebook_marketplace_property_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "category": "propertyrentals",
    "city_slug": "chicago",
    "min_price": 800,
    "max_price": 3500,
    "max_results": 20,
    "scrape_details": True
}

run = client.actor("unitbytes/facebook-marketplace-property-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("seller_name"), item.get("price"))
