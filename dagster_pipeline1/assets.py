import pandas as pd
import sqlite3
from dagster import asset, Output, AssetIn

DATABASE_PATH = "data_pipeline.db"

# 🚖 Load NYC Taxi Data
@asset
def table_1():
    """Loads NYC Taxi Trip data from CSV and saves to SQLite"""
    df = pd.read_csv("data/nyc_taxi.csv", parse_dates=["pickup_datetime", "dropoff_datetime"])
    
    # Save to SQLite
    conn = sqlite3.connect(DATABASE_PATH)
    df.to_sql("table_1", conn, if_exists="replace", index=False)
    conn.close()
    
    return Output(df)

# 🌦 Load Weather Data
@asset
def table_2():
    """Loads Weather data from CSV and saves to SQLite"""
    df = pd.read_csv("data/weather.csv", parse_dates=["timestamp"])

    # Save to SQLite
    conn = sqlite3.connect(DATABASE_PATH)
    df.to_sql("table_2", conn, if_exists="replace", index=False)
    conn.close()

    return Output(df)

# 🔄 Join Taxi & Weather Data
@asset(ins={"table_1": AssetIn("table_1"), "table_2": AssetIn("table_2")})
def joined_table(table_1: pd.DataFrame, table_2: pd.DataFrame):
    """Join Taxi Trips with Weather Data based on timestamp"""
    table_1["hour"] = table_1["pickup_datetime"].dt.floor("H")
    table_2["hour"] = table_2["timestamp"].dt.floor("H")
    
    merged_df = table_1.merge(table_2, on="hour", how="left").drop(columns=["hour"])

    # Save to SQLite
    conn = sqlite3.connect(DATABASE_PATH)
    merged_df.to_sql("joined_table", conn, if_exists="replace", index=False)
    conn.close()

    return Output(merged_df)

