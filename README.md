# 🚗 Facebook Marketplace Scraper API Suite: Local Deals, Used Cars, Real Estate & Listing Status (`$1.50 / 1K`)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt)
[![Open in Colab](https://img.shields.io/badge/Open_in-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/unitbytes/Facebook-Marketplace-Scraper-API/blob/main/notebooks/quickstart.ipynb)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Release](https://img.shields.io/github/v/release/unitbytes/Facebook-Marketplace-Scraper-API?style=for-the-badge&logo=github&color=10b981)](https://github.com/unitbytes/Facebook-Marketplace-Scraper-API/releases)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt)

**Zero-login Facebook Marketplace Scraper API suite on Apify (`$1.50 / 1,000 items`). Extract local classified deals, used cars & odometer mileage, rental & real estate properties, seller ratings, GPS coordinates, HD photo carousels, and live sold/available status checks across 100+ countries.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt) • [**📓 Open in Google Colab**](https://colab.research.google.com/github/unitbytes/Facebook-Marketplace-Scraper-API/blob/main/notebooks/quickstart.ipynb) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 41 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-facebook-marketplace-deals-car-scraper-banner.jpg" alt="🚗 Facebook Marketplace Scraper API Suite: Local Deals, Used Cars, Real Estate & Listing Status (`$1.50 / 1K`)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's `$5` free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, Google Colab, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, an **interactive 1-Click Google Colab notebook (`notebooks/quickstart.ipynb`)**, **9-node n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **Facebook Marketplace Scraper: Cars, Rentals & Deals API**<br><sub>[`unitbytes/Facebook-Marketplace-Scraper`](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt) • [Full Schema](https://unitbytes.com/actors/facebook-marketplace-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_facebook_marketplace_scraper.py`](examples/run_facebook_marketplace_scraper.py) | [`n8n/facebook-marketplace-scraper-n8n-workflow.json`](n8n/facebook-marketplace-scraper-n8n-workflow.json) | [`JSON`](samples/facebook-marketplace-scraper-sample.json) · [`CSV`](samples/facebook-marketplace-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt) |
| **Facebook Marketplace Vehicle Scraper: Cars, VIN & Mileage**<br><sub>[`unitbytes/facebook-marketplace-vehicle-scraper`](https://apify.com/unitbytes/facebook-marketplace-vehicle-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) • [Full Schema](https://unitbytes.com/actors/facebook-marketplace-vehicle-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_facebook_marketplace_vehicle_scraper.py`](examples/run_facebook_marketplace_vehicle_scraper.py) | [`n8n/facebook-marketplace-vehicle-scraper-n8n-workflow.json`](n8n/facebook-marketplace-vehicle-scraper-n8n-workflow.json) | [`JSON`](samples/facebook-marketplace-vehicle-scraper-sample.json) · [`CSV`](samples/facebook-marketplace-vehicle-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/facebook-marketplace-vehicle-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) |
| **Facebook Marketplace Property & Rentals Scraper**<br><sub>[`unitbytes/facebook-marketplace-property-scraper`](https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) • [Full Schema](https://unitbytes.com/actors/facebook-marketplace-property-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_facebook_marketplace_property_scraper.py`](examples/run_facebook_marketplace_property_scraper.py) | [`n8n/facebook-marketplace-property-scraper-n8n-workflow.json`](n8n/facebook-marketplace-property-scraper-n8n-workflow.json) | [`JSON`](samples/facebook-marketplace-property-scraper-sample.json) · [`CSV`](samples/facebook-marketplace-property-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) |
| **Facebook Marketplace Details & Status Checker (Sold/Price)**<br><sub>[`unitbytes/facebook-marketplace-status-checker`](https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_fb_mkt) • [Full Schema](https://unitbytes.com/actors/facebook-marketplace-status-checker/) • [Engineering Playbook](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)</sub> | [`examples/run_facebook_marketplace_status_checker.py`](examples/run_facebook_marketplace_status_checker.py) | [`n8n/facebook-marketplace-status-checker-n8n-workflow.json`](n8n/facebook-marketplace-status-checker-n8n-workflow.json) | [`JSON`](samples/facebook-marketplace-status-checker-sample.json) · [`CSV`](samples/facebook-marketplace-status-checker-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_fb_mkt) |

- 📓 **1-Click Interactive Google Colab Notebook:** Open [`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb) directly in your browser via [**Google Colab ↗**](https://colab.research.google.com/github/unitbytes/Facebook-Marketplace-Scraper-API/blob/main/notebooks/quickstart.ipynb) to inspect sample DataFrames and test live API queries with zero local setup.
- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 41 pre-built 9-node scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbooks:** [**Classifieds Arbitrage Playbook**](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/) • [**Used Car VIN & Auto Leads Playbook**](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/) — or browse all guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **Extract Facebook Marketplace Used Cars with 17-Digit VIN & Mileage** | Scrape private-party and dealer car/truck listings on Facebook Marketplace with parsed year, make, model, odometer mileage, and VINs. | [⚡ Run Task Preset](https://apify.com/unitbytes/facebook-marketplace-vehicle-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) |
| **Scrape Facebook Marketplace Apartments, Houses & Off-Market Rentals** | Extract rental and property listings on Facebook Marketplace with bedroom/bathroom counts, square footage, pet policies, and GPS coordinates. | [⚡ Run Task Preset](https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_fb_mkt) |
| **Verify Facebook Marketplace LIVE / SOLD Status & Price Drops** | Audit batches of Facebook Marketplace listing URLs to detect SOLD items, removed listings, price reductions, and real days-on-market. | [⚡ Run Task Preset](https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_fb_mkt) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 Facebook Marketplace Scraper: Cars, Rentals & Deals API (`unitbytes/Facebook-Marketplace-Scraper`)

<p align="center">
  <a href="https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-facebook-marketplace-scraper-banner.jpg" alt="Facebook Marketplace Scraper: Cars, Rentals & Deals API" width="100%" />
  </a>
</p>

Scrape Facebook Marketplace vehicles (VIN, mileage, make/model), apartment rentals (beds, baths, sqft, walk score), seller profiles, and local deals across multiple cities or ZIP codes.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` search item, `$0.0035` full listing detail (Gold+ tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt](https://apify.com/unitbytes/Facebook-Marketplace-Scraper?fpr=939u3w&fp_sid=gh_fb_mkt)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/facebook-marketplace-scraper/](https://unitbytes.com/actors/facebook-marketplace-scraper/)
- **n8n Workflow File:** [`n8n/facebook-marketplace-scraper-n8n-workflow.json`](n8n/facebook-marketplace-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Automating Local Classifieds Arbitrage: Scraping Facebook Marketplace, Craigslist & OfferUp](https://unitbytes.com/blog/local-classifieds-arbitrage-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Bypass Facebook 1,000 Listing Ceiling:** Autonomous spatial grid partitioning allows extracting tens of thousands of items across nationwide zip codes.
- **40+ Granular Extraction Fields:** Vehicle mileage, transmission, VIN, exterior color, rental bed/bath counts, square footage, and seller profile rating.
- **100% Zero Login Architecture:** Never risk your Facebook personal account or proxy burn. Scrapes completely unauthenticated with zero cookies.
- **Permanent HD Image URLs:** Extracts original high-resolution photo URLs directly from Facebook CDN without compression artifacts.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `start_urls` | `array` | — | List of Facebook Marketplace Search URLs, Category URLs, Seller Profile URLs (/marketplace/profile/<id>/), Item URLs (/marketplace/item/<id>/), or raw Item IDs. Overrides search query if provided. |
| `search_query` | `string` | `iphone` | What to search for (e.g. 'iphone', 'toyota camry', 'apartments'). Supports comma-separated batch queries (e.g. 'honda civic, toyota corolla, mazda 3'). Leave empty when browsing a Category preset. |
| `city_slug` | `string` | `sanfrancisco` | Target marketplace city slug (e.g. 'sanfrancisco', 'newyork', 'chicago'), 5-digit US ZIP code (e.g. '90210'), or comma-separated multi-city list (e.g. 'austin, dallas, houston'). |
| `category` | `string` | `all` | Filter by official Facebook Marketplace category, or browse an entire category feed without a keyword. |
| `min_price` | `integer` | `0` | Minimum listing price in local currency. |
| `max_price` | `integer` | `50000` | Maximum listing price in local currency. |
| `max_results` *(Required)* | `integer` | `20` | Maximum number of listings to scrape. |
| `scrape_details` | `boolean` | `True` | Fetch full listing detail pages via GraphQL for complete descriptions, 10-30+ HD photo carousels, VINs, walk scores, and seller ratings. Disable for ultra-fast, low-cost discovery mode (still extracts price, status, year/mileage, beds/baths/sqft, seller ID, and primary photo). |
| `include_all_photos` | `boolean` | `True` | When Deep Inspection is enabled, scrape the full high-resolution photo carousel (10-30+ HD photos) and videos. Disable to fetch only the primary listing photo for faster runs. |
| `sort_by` | `string` | `best_match` | How to sort the marketplace results. |
| `days_since_listed` | `integer` | `7` | Only scrape listings posted within this many days (1 = last 24h, 7 = last week, 30 = last month). |
| `item_condition` | `string` | `all` | Filter by item condition upstream on Facebook Marketplace. |
| `delivery_method` | `string` | `all` | Filter by local pickup vs. nationwide shipping. |
| `exact_match` | `boolean` | `False` | When enabled, sets exact=true upstream on Facebook Marketplace to exclude broad fuzzy keyword expansions. |
| `radius` | `integer` | `500` | Search radius in kilometers (default 500 for broad regional coverage; reduce to 20-50 km for tight city-level searches). Max 500. |
| `min_year` | `integer` | — | Minimum vehicle model year (e.g. 2015). |
| `max_year` | `integer` | — | Maximum vehicle model year (e.g. 2024). |
| `min_mileage` | `integer` | — | Minimum vehicle odometer reading (miles/km). |

#### Python SDK Quickstart (`examples/run_facebook_marketplace_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/facebook-marketplace-scraper-sample.json`)
```json
{
  "id": "1000000000000003",
  "url": "https://www.facebook.com/marketplace/item/1000000000000003/",
  "title": "1998 Toyota Camry LE Sedan 4D",
  "price": "$5,500",
  "city": "Los Angeles",
  "state": "CA",
  "condition": "Used - Good",
  "category": "Vehicles > Cars & Trucks > Sedans",
  "description": "Clean title, 1 owner vehicle. Recently serviced with new brakes and tires. Call or text 555-123-4567 for test drive.",
  "images": [
    "https://scontent.xx.fbcdn.net/v/t39.30808-6/example_camry_front.jpg",
    "https://scontent.xx.fbcdn.net/v/t39.30808-6/example_camry_interior.jpg",
    "https://scontent.xx.fbcdn.net/v/t39.30808-6/example_camry_engine.jpg"
  ],
  "make": "Toyota",
  "model": "Camry",
  "trim": "LE Sedan 4D",
  "year": 1998,
  "mileage": 142000,
  "transmission": "AUTOMATIC",
  "fuel_type": "GASOLINE",
  "seller_type": "PRIVATE_SELLER",
  "seller_phone": null,
  "pseudo_seller_id": "anon_1c373039bfed8879",
  "is_sold": false,
  "is_pending": false
}
```

#### Frequently Asked Questions
**Q: Do I need a Facebook account or cookies to scrape Facebook Marketplace?**
No. All UnitBytes Facebook Marketplace engines run 100% cookieless in the cloud, so you never risk personal Facebook accounts or manage browser sessions.

**Q: Can I search across multiple cities or ZIP codes in one run?**
Yes. Pass any list of US/global cities or ZIP codes along with search keywords, category filters, minimum/maximum price bounds, and kilometer/mile radius.

**Q: Does it detect price drops and SOLD listing status?**
Yes. Every record includes current price, strikethrough previous_price, price-drop flags, live/pending/sold availability, GPS coordinates, and high-resolution photos.

**Q: How much does the Facebook Marketplace Scraper cost?**
Runs cost `$0.0015` per listing (`$1.50` per 1,000 items, with volume tiers down to `$1.00/1K`) and include a free monthly credit on Apify.

---

### 🚀 Facebook Marketplace Vehicle Scraper: Cars, VIN & Mileage (`unitbytes/facebook-marketplace-vehicle-scraper`)

Scrape used cars, trucks, and motorcycles from Facebook Marketplace by city, ZIP code, make, model, year, and mileage. Extracts 17-digit VIN, odometer mileage, transmission, fuel type, and dealer vs. private seller status. No login required.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` search discovery listing, `$0.0035` full listing details & specifications (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/facebook-marketplace-vehicle-scraper?fpr=939u3w&fp_sid=gh_fb_mkt](https://apify.com/unitbytes/facebook-marketplace-vehicle-scraper?fpr=939u3w&fp_sid=gh_fb_mkt)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/facebook-marketplace-vehicle-scraper/](https://unitbytes.com/actors/facebook-marketplace-vehicle-scraper/)
- **n8n Workflow File:** [`n8n/facebook-marketplace-vehicle-scraper-n8n-workflow.json`](n8n/facebook-marketplace-vehicle-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **100% Upstream Vehicle Filtering:** Filter directly on Facebook Marketplace by min_year, max_year, min_mileage, max_mileage, make, model, transmission (automatic / manual), and body_style (suv, sedan, truck, coupe, van).
- **Complete Automotive Specs:** Automatically extracts year, make, model, trim, mileage, transmission, fuel_type, exterior_color, interior_color, and 17-character vin.
- **Private Seller vs. Dealership Detection:** Distinguishes "PRIVATE_SELLER" from "DEALERSHIP", extracts 5-star seller_rating & seller_review_count, and scrapes full dealership/seller catalogs via /marketplace/profile/<id>/.
- **Multi-City & Batch Model Search:** Search multiple cities or 5-digit US ZIP codes ("losangeles, dallas, 90210") and multiple models ("toyota camry, honda civic, ford f150") in a single run.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `search_query` | `string` | `toyota camry` | Search by vehicle keywords (e.g. 'toyota camry, honda civic, ford f150') or leave empty to browse all vehicles in the selected city. |
| `city_slug` | `string` | `losangeles` | Target city slug (e.g. 'losangeles', 'dallas', 'chicago'), 5-digit US ZIP code ('90210'), or comma-separated multi-city list ('austin, dallas, houston'). |
| `category` | `string` | `vehicles` | Facebook Marketplace vehicle category feed. |
| `min_price` | `integer` | `500` | Minimum vehicle price. |
| `max_price` | `integer` | `50000` | Maximum vehicle price. |
| `min_year` | `integer` | — | Minimum vehicle model year (e.g. 2014). Applied upstream on Facebook Marketplace. |
| `max_year` | `integer` | — | Maximum vehicle model year (e.g. 2024). Applied upstream on Facebook Marketplace. |
| `min_mileage` | `integer` | — | Minimum odometer reading. |
| `max_mileage` | `integer` | — | Maximum odometer reading (e.g. 120000). Applied upstream on Facebook Marketplace. |
| `make` | `string` | — | Filter by manufacturer slug or ID (e.g. 'toyota', 'honda', 'ford'). |
| `model` | `string` | — | Filter by model slug or ID (e.g. 'camry', 'civic', 'tacoma'). |
| `transmission` | `string` | `all` | Filter vehicles by transmission type. |
| `body_style` | `string` | — | Filter by body style (e.g. 'suv', 'sedan', 'truck', 'coupe', 'hatchback', 'van'). |
| `max_results` *(Required)* | `integer` | `20` | Maximum number of vehicles to scrape. |
| `scrape_details` | `boolean` | `True` | Enable Deep Inspection to extract 17-digit VIN, trim, fuel type, exterior/interior color, PRIVATE_SELLER vs. DEALERSHIP classification, 5-star seller ratings, and 10-30+ HD photos. Disable for ultra-fast discovery (still extracts year, mileage, price, and status). |
| `days_since_listed` | `integer` | `7` | Only include vehicles posted within this many days (1 = last 24h, 7 = past week, 30 = past month). |
| `sort_by` | `string` | `creation_time_descend` | Sort order for vehicle search. |
| `radius` | `integer` | `500` | Search radius in kilometers (up to 500km). |

#### Python SDK Quickstart (`examples/run_facebook_marketplace_vehicle_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "search_query": "toyota camry",
    "city_slug": "losangeles",
    "category": "vehicles",
    "min_price": 2000,
    "max_price": 15000,
    "max_results": 20
}

run = client.actor("unitbytes/facebook-marketplace-vehicle-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("seller_name"), item.get("price"))
```

#### Sample Output Schema (`samples/facebook-marketplace-vehicle-scraper-sample.json`)
```json
{
  "id": "1000000000000003",
  "url": "https://www.facebook.com/marketplace/item/1000000000000003/",
  "title": "2017 Toyota Camry · SE Sedan 4D",
  "price": "$10,600",
  "numeric_price": 10600.0,
  "currency": "USD",
  "listing_status": "ACTIVE",
  "year": 2017,
  "make": "Toyota",
  "model": "Camry",
  "trim": "SE Sedan 4D",
  "mileage": 95000,
  "transmission": "AUTOMATIC",
  "fuel_type": "GASOLINE",
  "exterior_color": "Silver",
  "interior_color": "Black",
  "vin": "4T1BF1FK5HU123456",
  "seller_type": "PRIVATE_SELLER",
  "seller_name": "Chris D.",
  "seller_id": "100000123456789",
  "seller_profile_url": "https://www.facebook.com/marketplace/profile/100000123456789/",
  "seller_rating": 4.9,
  "seller_review_count": 14,
  "city_slug": "losangeles"
}
```

#### Frequently Asked Questions
**Q: What vehicle-specific fields are extracted from Facebook Marketplace?**
Extracts vehicle year, make, model, trim, odometer mileage, transmission type, exterior/interior color, fuel type, title status, price drops, and seller profile metadata.

**Q: Can I filter by maximum mileage, model year, or price range?**
Yes. Configure minPrice, maxPrice, minYear, maxYear, maxMileage, and transmission filters across any city or ZIP code radius.

**Q: How can dealerships and car flippers spot under-market vehicles?**
Combine sortBy: creation_time_descend (newest listings) with our automated n8n Deal Scoring workflow to get instant alerts when low-mileage private-party cars are listed.

**Q: Do I need a Facebook login or residential proxies?**
No. Proxy rotation and cookieless session handling are built in at `$1.00` per 1,000 vehicles.

---

### 🚀 Facebook Marketplace Property & Rentals Scraper (`unitbytes/facebook-marketplace-property-scraper`)

Scrape apartments for rent, houses for rent, and homes for sale on Facebook Marketplace. Filter by bedrooms, bathrooms, square footage, price, and city/ZIP. Extracts beds, baths, sqft, pet policy, laundry, parking, walk score, and landlord profiles.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` search discovery listing, `$0.0035` full listing details & specifications (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_fb_mkt](https://apify.com/unitbytes/facebook-marketplace-property-scraper?fpr=939u3w&fp_sid=gh_fb_mkt)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/facebook-marketplace-property-scraper/](https://unitbytes.com/actors/facebook-marketplace-property-scraper/)
- **n8n Workflow File:** [`n8n/facebook-marketplace-property-scraper-n8n-workflow.json`](n8n/facebook-marketplace-property-scraper-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Apartments for Rent & Homes for Sale:** Extracts Facebook Marketplace property rentals and real estate listings across any city or ZIP code with zero Facebook account login or cookies required.
- **Structured Bedrooms, Bathrooms, SqFt & Amenities:** Captures property_type (Apartment, House, Townhouse, Condo), bedrooms, bathrooms, square_feet, pet_friendly policies, in-unit laundry, parking, and AC/heating details.
- **Exact GPS Coordinates & Price-Drop Tracking:** Returns latitude/longitude coordinates, postal codes, strikethrough previous_price comparisons, and listing availability (LIVE, PENDING, SOLD).
- **High-Res Property Galleries & Landlord Profiles:** Extracts full HD room photo arrays, landlord/agent profile names, and direct listing URLs ready for real estate comp analysis and lead pipelines.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `category` | `string` | `propertyrentals` | Choose between Property Rentals (apartments, houses, rooms for rent) or Property for Sale. |
| `city_slug` | `string` | `chicago` | Target city slug (e.g. 'newyork', 'sanfrancisco', 'chicago', 'miami'), 5-digit US ZIP code ('90210'), or comma-separated multi-city list ('austin, dallas, houston'). |
| `search_query` | `string` | — | Optional keyword filter (e.g. 'studio', 'loft', 'townhouse') or leave empty to scrape the full property category feed. |
| `min_price` | `integer` | `500` | Minimum monthly rent or sale price. |
| `max_price` | `integer` | `10000` | Maximum monthly rent or sale price. |
| `min_bedrooms` | `integer` | — | Minimum number of bedrooms (applied upstream on Facebook Marketplace). |
| `max_bedrooms` | `integer` | — | Maximum number of bedrooms. |
| `min_bathrooms` | `integer` | — | Minimum number of bathrooms. |
| `min_sqft` | `integer` | — | Minimum property square footage / area. |
| `max_sqft` | `integer` | — | Maximum property square footage / area. |
| `max_results` *(Required)* | `integer` | `20` | Maximum number of property listings to scrape. |
| `scrape_details` | `boolean` | `True` | Enable Deep Inspection to extract pet policy, laundry type, parking, heating/AC, street address, Walk/Transit/Bike scores, landlord ratings, and 10-30+ HD photos. Disable for ultra-fast discovery (still extracts price, bedrooms, bathrooms, and sqft). |
| `days_since_listed` | `integer` | `7` | Only include properties posted within this many days (1 = last 24h, 7 = past week, 30 = past month). |
| `sort_by` | `string` | `creation_time_descend` | Sort order for property search. |
| `start_urls` | `array` | — | Paste Facebook Marketplace property search URLs, landlord profile URLs (/marketplace/profile/<id>/), or listing URLs. |
| `proxy_configuration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Select proxies to be used by your scraper. |

#### Python SDK Quickstart (`examples/run_facebook_marketplace_property_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/facebook-marketplace-property-scraper-sample.json`)
```json
{
  "id": "1000000000000001",
  "url": "https://www.facebook.com/marketplace/item/1000000000000001/",
  "title": "2 Beds 1 Bath Apartment",
  "price": "$3,200",
  "numeric_price": 3200.0,
  "currency": "USD",
  "listing_status": "ACTIVE",
  "property_type": "Apartment",
  "bedrooms": 2,
  "bathrooms": 1,
  "square_feet": 920,
  "pet_friendly": "Cat and dog friendly",
  "laundry": "In-unit laundry",
  "parking": "Garage parking",
  "heating_ac": "Central AC",
  "street_address": "100 Main St",
  "walk_score": 96,
  "transit_score": 88,
  "bike_score": 94,
  "seller_name": "Taylor S.",
  "seller_rating": 4.85,
  "city_slug": "sanfrancisco"
}
```

#### Frequently Asked Questions
**Q: What rental and real estate fields are extracted?**
Extracts property_type (Apartment, House, Townhouse, Condo), bedrooms, bathrooms, square_feet, monthly rent or sale price, pet policy, laundry, parking, heating/AC, and GPS coordinates.

**Q: Can I filter properties by bedrooms, bathrooms, or monthly rent?**
Yes. Filter by minimum/maximum price, bedrooms, bathrooms, square footage, property type, and cat/dog friendly policies across any target city.

**Q: Does it capture full property photo galleries and landlord info?**
Yes. Every property record includes high-resolution room photos, full listing descriptions, neighborhood coordinates, and seller/landlord profile details.

**Q: How much does Facebook Marketplace Property extraction cost?**
Billed at `$1.00` per 1,000 property listings under Apify Pay-Per-Event with zero Facebook login required.

---

### 🚀 Facebook Marketplace Details & Status Checker (Sold/Price) (`unitbytes/facebook-marketplace-status-checker`)

Bulk check Facebook Marketplace item URLs, Item IDs, or Seller Profile URLs for real-time availability status (ACTIVE, SOLD, PENDING, REMOVED), price drops, full listing details, 5-star seller ratings, vehicle VINs, and rental specs. No login needed.

- **Pricing:** `$0.0015 / item` (Pay-Per-Event — `$0.0015` search discovery listing, `$0.0035` full listing details & specifications (volume tiers from `$0.0006`))
- **Cloud Console:** [https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_fb_mkt](https://apify.com/unitbytes/facebook-marketplace-status-checker?fpr=939u3w&fp_sid=gh_fb_mkt)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/facebook-marketplace-status-checker/](https://unitbytes.com/actors/facebook-marketplace-status-checker/)
- **n8n Workflow File:** [`n8n/facebook-marketplace-status-checker-n8n-workflow.json`](n8n/facebook-marketplace-status-checker-n8n-workflow.json)
- **Engineering Playbook:** [Used Car VIN, Auto Dealer & FSBO Real Estate Scraping Guide in 2026 (FB Marketplace, Craigslist & OfferUp)](https://unitbytes.com/blog/used-car-vin-real-estate-fsbo-scraping-facebook-marketplace-craigslist-offerup-guide/)

#### Key Capabilities
- **Real-Time Availability Status:** Returns normalized listing_status ("ACTIVE", "SOLD", "PENDING", "REMOVED"), is_sold, and is_pending flags for inventory synchronization and database cleanup.
- **Price Drop & Markdown Detection:** Extracts current price, clean numeric_price, currency, and previous strikethrough_price.
- **Full Listing Details by URL or ID:** Pass raw numeric Item IDs ("1000000000000002") or full item URLs to extract descriptions, condition, seller ratings, vehicle VIN/mileage, and property beds/baths/sqft.
- **Seller Profile Inventory Extraction:** Paste any /marketplace/profile/<seller_id>/ URL to list all active items sold by that user or dealership.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `start_urls` | `array` | `[{"url": "https://www.facebook.com/marketplace/p` | Paste one or more Facebook Marketplace item URLs (https://www.facebook.com/marketplace/item/123456789/), raw numeric Item IDs, or Seller Profile URLs (/marketplace/profile/<id>/) to check live status (ACTIVE, SOLD, PENDING) and extract full listing details. |
| `scrape_details` | `boolean` | `True` | Extracts full availability status (ACTIVE/SOLD/PENDING), price, markdowns, description, seller rating, vehicle/property specs, and photo gallery. |
| `include_all_photos` | `boolean` | `True` | Fetch the complete high-resolution photo gallery via GraphQL. |
| `fast_mode` | `boolean` | `False` | Skip per-item GraphQL detail inspection when scanning Seller Profile URLs. |
| `max_results` *(Required)* | `integer` | `50` | Maximum number of items to process (especially useful when passing Seller Profile URLs). |
| `concurrency` | `integer` | `5` | Number of listings to verify in parallel (1-10). |
| `proxy_configuration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Select proxies to be used by your scraper. |

#### Python SDK Quickstart (`examples/run_facebook_marketplace_status_checker.py`)
```python
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
```

#### Sample Output Schema (`samples/facebook-marketplace-status-checker-sample.json`)
```json
{
  "id": "1000000000000002",
  "url": "https://www.facebook.com/marketplace/item/1000000000000002/",
  "listing_status": "ACTIVE",
  "is_sold": false,
  "is_pending": false,
  "price": "$3,650",
  "numeric_price": 3650.0,
  "strikethrough_price": "$3,900",
  "currency": "USD",
  "title": "3 Beds 2 Baths - House",
  "seller_name": "Alex M.",
  "seller_id": "pfbid02exampleSellerProfileId123456",
  "seller_profile_url": "https://www.facebook.com/marketplace/profile/pfbid02exampleSellerProfileId123456/",
  "seller_rating": 5.0,
  "seller_review_count": 1
}
```

#### Frequently Asked Questions
**Q: How does the Facebook Marketplace Status Checker work?**
Pass up to 1,000 Facebook Marketplace listing URLs or numeric item IDs, and the Actor verifies in seconds whether each item is still LIVE, marked PENDING, SOLD, or REMOVED.

**Q: Does it track price cuts on active listings?**
Yes. Alongside live/sold availability, it returns the current price, formatted price string, and previous strikethrough price so you can detect seller price drops.

**Q: Why use this instead of re-running a full search scrape?**
Checking known item URLs directly is 5x faster and avoids re-scanning entire city feeds when syncing your database or removing sold cars/properties from your site.

**Q: Can I schedule recurring status checks in n8n or Make?**
Yes. Connect the Actor to a scheduled cron trigger in Apify or n8n to automatically mark sold inventory in PostgreSQL, Airtable, or Google Sheets.


---

## ⚡ Quick Installation & Local Usage

### 1. Run Interactively in Google Colab (Zero Local Setup)
Click **[Open in Google Colab ↗](https://colab.research.google.com/github/unitbytes/Facebook-Marketplace-Scraper-API/blob/main/notebooks/quickstart.ipynb)** ([`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb)) to inspect the sample output DataFrame immediately and run live extractions in your browser without installing Python locally.

### 2. Run Locally with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/Facebook-Marketplace-Scraper-API.git
cd Facebook-Marketplace-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_facebook_marketplace_scraper.py
```

### 3. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Configure your Apify API Token in the `HTTP Header Auth` credential on Node `2. Run UnitBytes (...)` (and customize your search inputs in Node `1. Configure Search & Rules`), then click **Test Workflow**.

### 4. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 41 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
