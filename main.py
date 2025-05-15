from utils.extract import fetch_product_data
from utils.transform import process_product_data
from utils.load import save_to_local_csv, save_to_google_sheets
from utils.load import save_to_postgresql



def main():
    base_url = 'https://fashion-studio.dicoding.dev/'
    product_collection = []

    print(f"Starting scrape on main page: {base_url}")
    try:
        initial_products = fetch_product_data(base_url)
        product_collection.extend(initial_products)
    except Exception as err:
        print(f"Error scraping main page: {err}")

    for page_number in range(2, 51):
        page_url = f"{base_url}page{page_number}"
        print(f"Scraping page {page_number}: {page_url}")
        try:
            page_products = fetch_product_data(page_url)
            product_collection.extend(page_products)
        except Exception as err:
            print(f"Error scraping page {page_number}: {err}")

    processed_data = process_product_data(product_collection)
    save_to_local_csv(processed_data)
    save_to_postgresql(processed_data)

    save_to_google_sheets(
        processed_data,
        '1UzOhodlr_hJ-62tXbQBGggXVRygdKbyNB6nnRB35LJY',
        'Sheet1!A2'
    )


if __name__ == '__main__':
    main()
