from dagster import HourlyPartitionsDefinition

# ⏳ Create hourly partitions for table_1
table_1_partitions = HourlyPartitionsDefinition(start_date="2024-01-01")
