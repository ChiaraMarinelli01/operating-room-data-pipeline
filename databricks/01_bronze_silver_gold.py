# Databricks-ready notebook/script
# The three layers illustrate a simple Medallion-style architecture.
#
# Bronze: raw data
# Silver: cleaned/validated data
# Gold: analytical aggregates

from pyspark.sql import functions as F

# Replace with your Databricks storage location.
RAW_PATH = "/Volumes/or_analytics/default/raw/surgeries_raw.csv"
SILVER_PATH = "/Volumes/or_analytics/default/silver/surgeries"
GOLD_PATH = "/Volumes/or_analytics/default/gold/specialty_metrics"

# BRONZE
bronze = (
    spark.read
    .option("header", True)
    .csv(RAW_PATH)
)

bronze.write.mode("overwrite").format("delta").saveAsTable(
    "or_analytics.bronze_surgeries"
)

# SILVER
silver = (
    bronze
    .withColumn("scheduled_date", F.to_date("scheduled_date"))
    .withColumn("duration_minutes", F.col("duration_minutes").cast("int"))
    .withColumn("waiting_minutes", F.col("waiting_minutes").cast("int"))
    .withColumn("emergency", F.col("emergency").cast("boolean"))
    .dropDuplicates(["surgery_id"])
    .filter(F.col("duration_minutes") > 0)
    .filter(F.col("waiting_minutes") >= 0)
)

silver.write.mode("overwrite").format("delta").saveAsTable(
    "or_analytics.silver_surgeries"
)

# GOLD
gold = (
    silver.groupBy("specialty")
    .agg(
        F.count("*").alias("number_of_surgeries"),
        F.round(F.avg("duration_minutes"), 1).alias("avg_duration"),
        F.round(F.avg("waiting_minutes"), 1).alias("avg_waiting"),
        F.round(F.avg(F.col("emergency").cast("double")) * 100, 2)
         .alias("emergency_pct"),
    )
)

gold.write.mode("overwrite").format("delta").saveAsTable(
    "or_analytics.gold_specialty_metrics"
)
