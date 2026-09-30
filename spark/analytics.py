"""Analytical transformations using Spark SQL/DataFrame API."""

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("OperatingRoomAnalytics").getOrCreate()

# Change this path when running in Databricks.
DATA_PATH = "data/processed/surgeries_spark.parquet"

df = spark.read.parquet(DATA_PATH)

print("=== SURGERIES BY SPECIALTY ===")
(
    df.groupBy("specialty")
      .agg(
          F.count("*").alias("surgeries"),
          F.round(F.avg("duration_minutes"), 1).alias("avg_duration"),
          F.round(F.avg("waiting_minutes"), 1).alias("avg_waiting"),
      )
      .orderBy(F.desc("surgeries"))
      .show()
)

print("=== HOSPITAL EMERGENCY RATE ===")
(
    df.groupBy("hospital")
      .agg(
          F.count("*").alias("surgeries"),
          F.round(
              F.avg(F.col("emergency").cast("double")) * 100, 2
          ).alias("emergency_pct"),
      )
      .orderBy(F.desc("emergency_pct"))
      .show()
)

spark.stop()
