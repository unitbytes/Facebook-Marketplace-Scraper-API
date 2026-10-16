#!/usr/bin/env python3
"""
Facebook Marketplace Scraper — Bypass 1K Limit, 40+ Fields — Official Python Quickstart
Actor: https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/facebook-marketplace-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/facebook-marketplace-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_facebook_marketplace_scraper.py
"""

import json
import os
from apify_client import ApifyClient

# Read API token from environment (or paste your token directly for local testing)
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")


def main():
    client = ApifyClient(APIFY_API_TOKEN)
    
    
    run_input = {
        "search_query": "iphone",
        "city_slug": "sanfrancisco",
        "min_price": 0,
        "max_price": 2000,
        "max_results": 2,
        "concurrency": 5,
        "days_since_listed": 30,
        "sort_by": "best_match"
    }
    
    run = client.actor("unitbytes/Facebook-Marketplace-Scraper").call(run_input=run_input)
    
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item.get("title"), item.get("price"), item.get("url"))


if __name__ == "__main__":
    main()
