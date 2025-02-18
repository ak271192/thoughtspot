
This project is a Dagster-based data pipeline that:
- Processes NYC Taxi Data & NOAA Weather Data
- Applies Pandas transformations
- Stores data in SQLite3
- Partitions Table 1 hourly (168 partitions for one week)
- Includes tests for validation
- Is easily reproducible & deployable

---

1. Setup Instructions

1.1 Install Prerequisites

Ensure you have Python 3.9+ and Homebrew installed.

For macOS:
brew install python sqlite3

For Linux:
sudo apt update && sudo apt install python3 sqlite3 -y

---

1.2 Clone the Repository
git clone https://github.com/ak271192/thoughtspot.git
cd thoughtspot

---

1.3 Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Activate venv (Mac/Linux)

---

1.4 Install Dependencies
pip install -r requirements.txt

---

2. Running the Dagster Pipeline

2.1 Start Dagster Web Server
dagster dev
- Open Dagster UI at http://localhost:3000
- Click "Launch Execution" for process_data_job

---

2.2 Run the Job via CLI
dagster job launch -f dagster_pipeline1/jobs.py --job process_data_job

---

2.3 Verify Data in SQLite
After running the pipeline, check the database:
sqlite3 data_pipeline.db

Run:
SELECT * FROM table_1 LIMIT 5;
SELECT * FROM table_2 LIMIT 5;
SELECT * FROM joined_table LIMIT 5;

---

3. Running Tests

3.1 Ensure Virtual Environment is Activated
source venv/bin/activate

3.2 Run Pytest
pytest -v dagster_pipeline1/
Expected output:
All tests passed!

---

4. Folder Structure

dagster_pipeline/
│── dagster_pipeline/
│    ├── assets.py        # Dagster assets for tables
│    ├── jobs.py          # Dagster jobs
│    ├── partitions.py    # Partitioning logic
│    ├── repository.py    # Dagster repository
│    ├── tests.py         # Pipeline tests
│── data/                 # Static datasets (CSV files)
│    ├── nyc_taxi.csv     # NYC taxi data
│    ├── weather.csv      # Weather data
│── workspace.yaml        # Dagster workspace config
│── requirements.txt      # Dependencies
│── Dockerfile            # Docker setup
│── README.md             # Setup instructions
│── pyproject.toml        # Dagster settings

---

5. Deployment (Optional)

5.1 Run in Docker
docker build -t dagster-pipeline .
docker run -p 3000:3000 dagster-pipeline



6. Troubleshooting

6.1 If dagster is not found
source venv/bin/activate
pip install dagster dagster-webserver

6.2 If pytest doesn’t detect tests
touch dagster_pipeline/__init__.py
pytest -v dagster_pipeline/

---


