# ETL Pipeline Project

## Description
This project is an ETL (Extract, Transform, Load) pipeline that scrapes product data from the website [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/), transforms the data, and stores it in multiple formats (CSV, Google Sheets, PostgreSQL). The project follows a modular structure and includes unit tests for each module.

## Project Structure
```
project_root/
├── utils/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── test/
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── main.py
├── products.csv
└── requirements.txt
└── submission.txt

## Installation

1. Clone the repository:
```
git clone https://github.com/totoro-07/Etl-Dicoding.git
cd etl-pipeline
```


2. Install the required packages:
```
pip install -r requirements.txt
```

## Running the Pipeline

To run the ETL pipeline, execute the following command:
```
python main.py
```

## Running Unit Tests
To run all unit tests, use:
```
python -m unittest discover -s test -p "test_*.py" -v
```

To run a specific test file:
```
python -m unittest test.test_extract
```

## Output
The pipeline will save the data in the following formats:
- CSV file: `products.csv`
- Google Sheets: Configured in `save_to_google_sheets()`
- PostgreSQL: Database named `fashiondb`
