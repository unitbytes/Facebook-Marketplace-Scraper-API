#!/usr/bin/env python3
"""
Facebook Marketplace Details & Status Checker (Sold/Price) — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/facebook-marketplace-status-checker/
n8n Template: https://unitbytes.com/n8n/workflows/facebook-marketplace-status-checker-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_facebook_marketplace_status_checker.py
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
            "url": "https://www.facebook.com/marketplace/profile/pfbid02exampleSellerProfileId123456/"
        }
    ],
    "scrape_details": True,
    "include_all_photos": True,
    "max_results": 50,
    "fast_mode": False
}

run = client.actor("unitbytes/facebook-marketplace-status-checker").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("seller_name"), item.get("price"))
