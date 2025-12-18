import time
from scraper import save_as_csv, scrape_walmart


def main():
    try:
        query = input("What you want to search for? : ")
        pages = input("How many pages you want to scrape? (max 5) : ")
        pages = int(pages) if pages.isdigit() else 1
        scrape_walmart(query, int(pages))
        save_as_csv()
    except Exception as error:
        print("-" * 100)
        print("Error occurred: ", error)
        print("-" * 100)


if __name__ == "__main__":
    main()
