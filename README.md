# Operating Room Data Pipeline & Analytics

End-to-end portfolio project demonstrating **Python, ETL, SQL, PostgreSQL and dashboarding** on synthetic operating-room data.

## Architecture

Raw CSV → Python/Pandas ETL → PostgreSQL → SQL analytics → Streamlit dashboard

## Why this project?

The project complements my MSc thesis in Applied Mathematics and Operations Research by focusing on the data-processing side of an operational analytics problem.

It demonstrates:
- data ingestion and cleaning
- validation and transformation with Python/Pandas
- relational database design with PostgreSQL
- analytical SQL queries
- reproducible ETL
- dashboard development
- basic testing

## Tech stack

Python · Pandas · NumPy · SQL · PostgreSQL · SQLAlchemy · Streamlit · Docker · pytest

## Project structure

```text
.
├── data/
│   └── raw/
├── dashboard/
│   └── app.py
├── sql/
│   ├── schema.sql
│   └── analysis.sql
├── src/
│   ├── analysis.py
│   └── etl.py
├── tests/
│   └── test_etl.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Run locally

### 1. Create environment

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Run the ETL pipeline

```bash
python -m src.etl
```

This cleans the raw dataset, writes the processed data and loads the result into PostgreSQL.

### 4. Run tests

```bash
pytest
```

### 5. Launch the dashboard

```bash
streamlit run dashboard/app.py
```

Open the local URL shown by Streamlit.

## Data

The included dataset is **synthetic** and generated for portfolio/educational purposes. It does not contain real patient information.

## Roadmap

- [x] Python ETL
- [x] PostgreSQL database
- [x] SQL analytics
- [x] Dashboard
- [x] Automated tests
- [ ] PySpark implementation
- [ ] Databricks implementation
- [ ] CI/CD with GitHub Actions


## Version 2 — PySpark & Databricks

The project also includes a distributed-processing implementation:

```text
Raw CSV
   ↓
PySpark
   ↓
Parquet
   ↓
Spark analytics
```

and a Databricks-ready Bronze/Silver/Gold implementation using Delta tables.

### Run PySpark locally

After installing the optional PySpark dependency:

```bash
pip install pyspark
```

Run:

```bash
spark-submit spark/spark_etl.py
```

Then run:

```bash
spark-submit spark/analytics.py
```

The Databricks implementation is in `databricks/01_bronze_silver_gold.py`.

## Version 2 skills demonstrated

- PySpark DataFrame API
- Spark transformations and aggregations
- Parquet
- partitioning
- Spark SQL concepts
- Delta Lake
- Databricks-ready ETL
- Bronze / Silver / Gold architecture
- separation of local and cloud execution
