import requests
import pandas as pd
import json

def fetch_gdp_data(year: int = 2024):
    url = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD"
    params = {"date": str(year), "format": "json", "per_page": 20000}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data

def transform_gdp_data(data):
    records = data[1]
    df = pd.DataFrame(records)
    df["country_name"] = df["country"].apply(lambda x: x.get("value") if isinstance(x, dict) else None)
    df["country_code_iso2"] = df["country"].apply(lambda x: x.get("id") if isinstance(x, dict) else None)
    df = df[["country_name", "country_code_iso2", "countryiso3code", "date", "value"]]
    df.rename(columns={"countryiso3code": "iso3", "value": "GDP (current USD)"}, inplace=True)
    df["GDP (current USD)"] = pd.to_numeric(df["GDP (current USD)"], errors="coerce").round(0).astype("Int64")
    return df

def load_countries_data(file_path):
    df = pd.read_csv(file_path)
    return df

def merge_datasets(df_countries, df_gdp):
    merged_df = pd.merge(df_countries, df_gdp, on="iso3", how="left")
    cols_order = [
        "country", "capital", "region", "continents", "area", "population",
        "iso2", "iso3", "date", "GDP (current USD)"
    ]
    merged_df = merged_df[cols_order]
    return merged_df

def save_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"✅ CSV saved to {file_path}")

if __name__ == "__main__":
    countries_file = r"C:\Users\Admin\Downloads\all_countries.csv"
    json_file = "worldbank_gdp_2024.json"
    csv_file = "merged_country_gdp_2024.csv"

    gdp_json = fetch_gdp_data(year=2024)
    save_json(gdp_json, json_file)
    df_gdp = transform_gdp_data(gdp_json)
    df_countries = load_countries_data(countries_file)
    merged_df = merge_datasets(df_countries, df_gdp)
    save_csv(merged_df, csv_file)
    print(merged_df.head())
