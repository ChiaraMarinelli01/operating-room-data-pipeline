# Architecture

## Version 1

```text
CSV
 ↓
Python / Pandas
 ↓
PostgreSQL
 ↓
SQL
 ↓
Streamlit
```

## Version 2

```text
                    ┌───────────────┐
                    │   Raw CSV     │
                    └───────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
       Python / Pandas               PySpark
              ↓                           ↓
        PostgreSQL                    Parquet
              ↓                           ↓
          SQL analytics            Spark analytics
              ↓
          Dashboard
                                          │
                                          ↓
                                   Databricks / Delta
                                          │
                             ┌────────────┴────────────┐
                             ↓                         ↓
                          Silver                      Gold
                       cleaned data              BI / analytics
```

## Why two pipelines?

The Pandas pipeline is useful for local data processing and relational analytics.

The Spark pipeline demonstrates how the same processing logic can be expressed in a distributed-data framework.

The Databricks layer demonstrates a cloud-oriented Bronze/Silver/Gold architecture.
