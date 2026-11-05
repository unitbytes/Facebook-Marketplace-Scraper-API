#!/usr/bin/env python3
"""
Facebook Marketplace Seller Scraper: Profile & Inventory — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/facebook-marketplace-seller-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/facebook-marketplace-seller-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/facebook-marketplace-seller-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_facebook_marketplace_seller_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "start_urls": [
        {
            "url": "https://www.facebook.com/marketplace/item/1640264554118295/"
        }
    ],
    "include_sold": True,
    "deep_pagination": True,
    "max_items_per_seller": 100
}

run = client.actor("unitbytes/facebook-marketplace-seller-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("seller_name"), item.get("city_display_name"), item.get("seller_rating"))
