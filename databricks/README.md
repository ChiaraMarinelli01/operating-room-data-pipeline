# Databricks

This folder contains a Databricks-ready implementation of the pipeline.

## Architecture

```text
Raw CSV
   ↓
Bronze Delta table
   ↓
Silver Delta table
   ↓
Gold analytical table
   ↓
Dashboard / BI
```

The implementation uses PySpark and Delta tables.

The paths in `01_bronze_silver_gold.py` are placeholders for a Databricks Volume.
They must be changed to the storage available in the user's Databricks workspace.

## Suggested Databricks setup

1. Create a Databricks workspace.
2. Create a catalog/schema for the project.
3. Upload the synthetic CSV to a Volume.
4. Import `01_bronze_silver_gold.py` as a notebook/script.
5. Run the Bronze → Silver → Gold pipeline.
6. Inspect the resulting Delta tables with SQL.
7. Optionally connect the Gold table to a BI tool.

No cloud credentials or secrets are stored in this repository.
