from dagster import define_asset_job
from .assets import table_1, table_2, joined_table

# 🚀 Define a job that processes all tables
process_data_job = define_asset_job(
    "process_data", selection=[table_1, table_2, joined_table]
)
