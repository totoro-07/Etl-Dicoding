import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)


def fetch_product_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise Exception(f"Failed to retrieve URL: {url}. Error: {err}")

    try:
        page_content = BeautifulSoup(response.text, 'html.parser')
        item_list = []

        for card in page_content.find_all('div', class_='collection-card'):
            title_element = card.find('h3', class_='product-title')
            title = title_element.text.strip() if title_element else 'Unknown Title'

            price_element = card.find('div', class_='price-container')
            price = price_element.text.strip() if price_element else 'Price Unavailable'

            rating_element = card.find('p', string=lambda text: text and 'Rating' in text)
            rating = rating_element.text.strip() if rating_element else 'No Rating'

            colors_element = card.find('p', string=lambda text: text and 'Colors' in text)
            colors = colors_element.text.strip() if colors_element else 'No Color Info'

            size_element = card.find('p', string=lambda text: text and 'Size' in text)
            size = size_element.text.strip() if size_element else 'No Size Info'

            gender_element = card.find('p', string=lambda text: text and 'Gender' in text)
            gender = gender_element.text.strip() if gender_element else 'No Gender Info'

            item_list.append({
                'title': title,
                'price': price,
                'rating': rating,
                'colors': colors,
                'size': size,
                'gender': gender
            })

        return item_list
    except Exception as err:
        raise Exception(f"HTML Parsing Failed. Error: {err}")
