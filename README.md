# World Bank GDP and Country Data (2024)

This repository contains GDP data for all countries in 2024, merged with country metadata such as capital, region, population, and area. The data is sourced from the [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) and includes both raw JSON and cleaned CSV files.

## Contents

- `worldbank_gdp_2024.json` – Raw GDP JSON data fetched from the World Bank API.
- `all_countries.csv` – Country metadata including capital, region, continent, ISO codes, population, and area.
- `merged_country_gdp_2024.csv` – Cleaned and merged dataset combining GDP and country metadata.
- `script.py` – Python script used to fetch, clean, transform, and merge the data.

## Features

- Fetches GDP data for all countries for a specific year using the World Bank API.
- Cleans and transforms the JSON data into a readable DataFrame.
- Merges GDP data with country metadata for richer analysis.
- Exports both JSON and CSV files for downstream use.

## Requirements

- Python 3.7+
- Pandas
- Requests

Install dependencies using pip:

```bash
pip install pandas requests
