import pandas as pd
import pytest
from dagster_pipeline.assets import table_1, table_2, joined_table

# Test if Table 1 (NYC Taxi Data) is loaded correctly
def test_table_1():
    df = table_1().value
    assert isinstance(df, pd.DataFrame)
    assert "trip_id" in df.columns
    assert "pickup_datetime" in df.columns

# Test if Table 2 (Weather Data) is loaded correctly
def test_table_2():
    df = table_2().value
    assert isinstance(df, pd.DataFrame)
    assert "weather_id" in df.columns
    assert "temperature" in df.columns

# Test if Join Operation Works Correctly
def test_joined_table():
    df_1 = table_1().value
    df_2 = table_2().value
    df_joined = joined_table(df_1, df_2).value
    assert isinstance(df_joined, pd.DataFrame)
    assert "trip_id" in df_joined.columns
    assert "temperature" in df_joined.columns
