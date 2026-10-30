#!/usr/bin/env python3
"""
Facebook Marketplace Scraper: Cars, Rentals & Deals API — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/facebook-marketplace-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/facebook-marketplace-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_facebook_marketplace_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "search_query": "iphone",
    "city_slug": "sanfrancisco",
    "category": "all",
    "min_price": 0,
    "max_price": 50000,
    "max_results": 20
}

run = client.actor("unitbytes/Facebook-Marketplace-Scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("url"))
