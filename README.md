# Operating Room Data Pipeline & Analytics

End-to-end Data Engineering portfolio project for processing and analysing synthetic operating-room data.

The project demonstrates two complementary data processing pipelines:

* a **Python/Pandas + PostgreSQL pipeline** for data ingestion, cleaning, relational storage and SQL analytics;
* a **PySpark + Databricks pipeline** following a **Bronze/Silver/Gold (Medallion) architecture** for distributed data processing and analytical transformations.

The project also includes data-quality validation, automated tests, Docker-based services and a Streamlit dashboard for data visualisation.

## Project Overview

The pipeline processes synthetic operating-room data from raw CSV files to cleaned datasets, analytical outputs and dashboard visualisations.

The project demonstrates practical Data Engineering workflows including:

* data ingestion and transformation;
* data cleaning and validation;
* relational database loading;
* SQL-based analytics;
* distributed processing with PySpark;
* Medallion architecture with Bronze, Silver and Gold layers;
* data-quality checks and automated testing;
* containerisation with Docker;
* analytical dashboard development with Streamlit.

## Architecture

### Python / PostgreSQL pipeline

```text
Raw CSV
   |
   v
Python / Pandas ETL
   |
   v
Cleaned data
   |
   v
PostgreSQL
   |
   +---- SQL analytics
   |
   +---- Streamlit dashboard
```

### PySpark / Databricks pipeline

```text
Raw CSV
   |
   v
PySpark
   |
   v
Bronze
   |
   v
Silver
   |
   v
Gold
   |
   +---- Analytical aggregates
```

## Technologies

* Python
* Pandas
* PySpark
* PostgreSQL
* SQL
* Databricks
* Docker
* Streamlit
* pytest

## Project Goal

The goal of the project is to demonstrate an end-to-end Data Engineering workflow using a realistic synthetic healthcare dataset, while comparing a traditional Python/relational approach with a distributed PySpark/Medallion architecture.

The project is intended as a portfolio example showcasing data ingestion, transformation, validation, storage, analytics and visualisation.
