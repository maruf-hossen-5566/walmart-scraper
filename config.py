import os
from dotenv import load_dotenv

load_dotenv()

BRIGHTDATA_API_KEY = os.getenv("BRIGHTDATA_API_KEY")
BRIGHTDATA_ZONE = os.getenv("BRIGHTDATA_ZONE")
BRIGHTDATA_ENDPOINT = os.getenv("BRIGHTDATA_ENDPOINT")

TIMEOUT = 60
MAX_PAGES = 5
OUTPUT_JSON = "data/data.json"
OUTPUT_CSV = "data/data.csv"
