# Walmart Product Scraper (Bright Data API)

A **pure Python Walmart scraper** that extracts structured product data directly from Walmart’s internal `__NEXT_DATA__`
JSON using **Bright Data Web Scraping API**.

This project avoids browser automation (Playwright/Selenium) and instead uses a **stable, scalable, and production-style
approach**.

---

## 🔧 Tech Stack

- Python
- Bright Data Web Scraping API
- requests
- BeautifulSoup + lxml
- pandas (CSV export)
- uv (dependency management)

---

## ✨ Features

- Scrapes Walmart search results by keyword
- Handles pagination (with configurable page limit)
- Extracts rich product data (price, rating, availability, seller, etc.)
- Uses Walmart’s `__NEXT_DATA__` (JSON source of truth)
- Saves output as **JSON** and **CSV**
- No browser automation required

---

## 📁 Project Structure

```
walmart_scraper/
├── main.py
├── scraper.py
├── brightdata.py
├── config.py
├── data/
│ ├── data.json
│ └── data.csv
├── .env.example
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Create virtual environment

```
uv venv
```

### 2. Install dependencies

```
uv pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.evn` file using `.env.example`:

```
BRIGHTDATA_API_KEY=your_api_key_here
BRIGHTDATA_ENDPOINT=brightdata_api_endpoint
BRIGHTDATA_ZONE=your_zone_name
```

### 4. Run the scraper

```
uv run main.py
```

You'll be prompted for:

- search keywork
- number of page to scrape

---

## 📤 Output

- Json data -> `data/data.json`
- CSV data -> `data/data.csv`

---

## 🧠 Notes

- This scraper extracts data from Walmart’s internal JSON (__NEXT_DATA__) instead of fragile HTML selectors.
- Bright Data handles IP rotation, JavaScript rendering, and bot protection.
- Designed to be simple, reliable, and production-ready.

---

## ⚠️ Disclaimer

This project is for educational and portfolio purposes only.
Always respect website terms of service and applicable laws.