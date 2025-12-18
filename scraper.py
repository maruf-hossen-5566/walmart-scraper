import json
from urllib.parse import quote  # To encode query into url
import pandas as pd
from bs4 import BeautifulSoup

from brightdata import fetch_html
from config import (
    MAX_PAGES as max_pages,
    OUTPUT_JSON as json_file_path,
    OUTPUT_CSV as csv_file_path,
)


def clean_extracted_data(data: list[dict]):
    """Getting the fields we want from the data and cleaning it up a bit."""
    cleaned_items = []
    for item in data:
        if item.get("__typename", "") == "Product":
            try:
                cleaned_item = {
                    "__typename": item.get("__typename", "--"),
                    "id": item.get("id", "--"),
                    "us_item_id": item.get("usItemId", "--"),
                    "name": item.get("name", "--"),
                    "catalog_product_type": item.get("catalogProductType", "--"),
                    "thumbnail_url": item.get("imageInfo", {}).get(
                        "thumbnailUrl", "--"
                    ),
                    "item_type": item.get("itemType", "--"),
                    "category_path_id": item.get("category", {}).get(
                        "categoryPathId", "--"
                    ),
                    "buy_now_eligible": item.get("buyNowEligible", "--"),
                    "class_type": item.get("classType", "--"),
                    "average_rating": item.get("averageRating", "--"),
                    "number_of_reviews": item.get("numberOfReviews", "--"),
                    "seller_name": item.get("sellerName", "--"),
                    "url": f'https://walmart.com{item.get("canonicalUrl", "--")}',
                    "price": item.get("price", "--"),
                    "is_preowned": item.get("isPreowned", "--"),
                    "availability_status_display_value": item.get(
                        "availabilityStatusDisplayValue", "--"
                    ),
                    "availability_status": item.get("availabilityStatusV2", {}).get(
                        "value", "--"
                    ),
                    "image_url": item.get("image", "--"),
                    "is_out_of_stock": item.get("isOutOfStock", "--"),
                    "sales_unit": item.get("salesUnit", "--"),
                    "modular_stack_key": item.get("modularStackKey", "--"),
                    "short_description": item.get("shortDescription", "--"),
                    "brand": item.get("brand", "--"),
                    "average_weight": item.get("averageWeight", "--"),
                    "weight_increment": item.get("weightIncrement", "--"),
                    "additional_offer_count": item.get("additionalOfferCount", "--"),
                    "availability_in_nearbyStore": item.get(
                        "availabilityInNearbyStore", "--"
                    ),
                }
                cleaned_items.append(cleaned_item)
            except Exception as e:
                print("Error: ", e)

    return cleaned_items


def prepare_url(query: str, num_pages: int = 1):
    q = quote(query)
    url = f"https://www.walmart.com/search?q={q}&page={num_pages}"
    return url


def parse_raw_html_return_script_tag(html: str):
    """Parse the raw html using BeautifulSoup and return the script tag"""
    sp = BeautifulSoup(html, "lxml")
    script_tag = sp.find("script", attrs={"id": "__NEXT_DATA__"})

    if not script_tag:
        raise RuntimeError("`script_tag` not found!")
    return script_tag


def extract_data_from_script_tag(script_tag):
    """Extract the data from the script tag"""
    data = json.loads(script_tag.text)
    stacks = (
        data.get("props", {})
        .get("pageProps", {})
        .get("initialData", {})
        .get("searchResult", {})
        .get("itemStacks", [])
    )
    for stack in stacks:
        items = stack.get("items")
        if items:
            return items

    return []


def scrape_walmart(query: str, pages: int = max_pages):
    """Scrape walmart.com for the given query and save the data to a json file"""
    num_pages = min(pages, max_pages)

    print("🧹 Scraping started...")
    current_page = 1
    each_page_data = []
    while True:
        """Prepare the url for the current page"""
        url = prepare_url(query, current_page)

        """Fetching the raw html of the page"""
        raw_html = fetch_html(url)

        """Parse the html using BeautifulSoup"""
        script_tag = parse_raw_html_return_script_tag(raw_html)

        """Extract the data from the script tag"""
        data_from_script_tag = extract_data_from_script_tag(script_tag)

        """Clean the extracted data"""
        cleaned_data = clean_extracted_data(data_from_script_tag)
        each_page_data.extend(cleaned_data)

        print(f"--- Scraped page {current_page} of {num_pages} ---")

        current_page += 1
        if current_page > num_pages:
            break

    """Save the cleaned data to a json file"""
    save_as_json(each_page_data)


def save_as_json(data: list[dict]):
    """Save the data to a json file"""
    with open(f"{json_file_path}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Saved json data to {json_file_path}.")


def save_as_csv():
    with open(f"{json_file_path}", "r") as f:
        d = json.load(f)
        df = pd.DataFrame(d)
        df.to_csv(f"{csv_file_path}", index=False)
    print(f"✅ Saved data to {csv_file_path}.")
