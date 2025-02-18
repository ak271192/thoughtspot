from dagster import Definitions, load_assets_from_modules
from . import assets, jobs

# 🎯 Load assets and jobs into Dagster
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[jobs.process_data_job],  # Add the job here
)
