
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine


def save_to_local_csv(dataframe, filename="products.csv"):
    dataframe.to_csv(filename, index=False)


def save_to_google_sheets(dataframe, spreadsheet_id, range_name):
    try:
        creds = Credentials.from_service_account_file('google-sheets-api.json')
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        values = [dataframe.columns.values.tolist()] + dataframe.values.tolist()
        body = {'values': values}

        result = sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        print(f"Data saved to Google Sheets at: {result.get('updatedRange')}")
    except Exception as err:
        print(f"Error saving to Google Sheets: {err}")


def save_to_postgresql(dataframe, table_name='products'):
    try:
        username, password, host, port, database = 'postgres', '12345678', '127.0.0.1', '5432', 'fashiondb'
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully saved to PostgreSQL table '{table_name}'.")
    except Exception as err:
        print(f"Error saving to PostgreSQL: {err}")