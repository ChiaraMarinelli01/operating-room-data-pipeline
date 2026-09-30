"""
PySpark version of the ETL pipeline.

Local:
    spark-submit spark/spark_etl.py

Databricks:
    Upload/copy this file to a Databricks workspace and run it as a job.
"""

from pathlib import Path
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, BooleanType, DateType
)

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = str(ROOT / "data" / "raw" / "surgeries_raw.csv")
OUTPUT_PATH = str(ROOT / "data" / "processed" / "surgeries_spark.parquet")

schema = StructType([
    StructField("surgery_id", StringType(), False),
    StructField("patient_id", StringType(), False),
    StructField("specialty", StringType(), False),
    StructField("hospital", StringType(), False),
    StructField("room_id", StringType(), False),
    StructField("scheduled_date", DateType(), False),
    StructField("start_time", StringType(), False),
    StructField("duration_minutes", IntegerType(), False),
    StructField("waiting_minutes", IntegerType(), False),
    StructField("emergency", IntegerType(), False),
    StructField("outcome", StringType(), False),
])


def build_spark():
    return (
        SparkSession.builder
        .appName("OperatingRoomETL")
        .getOrCreate()
    )


def transform(df):
    return (
        df
        .dropDuplicates(["surgery_id"])
        .filter(F.col("duration_minutes") > 0)
        .filter(F.col("waiting_minutes") >= 0)
        .withColumn("emergency", F.col("emergency").cast("boolean"))
        .withColumn("year", F.year("scheduled_date"))
        .withColumn("month", F.month("scheduled_date"))
        .withColumn(
            "is_long_surgery",
            F.when(F.col("duration_minutes") >= 180, True).otherwise(False)
        )
    )


def main():
    spark = build_spark()

    raw = (
        spark.read
        .option("header", True)
        .schema(schema)
        .option("dateFormat", "yyyy-MM-dd")
        .csv(RAW_PATH)
    )

    clean = transform(raw)

    (
        clean.write
        .mode("overwrite")
        .partitionBy("year", "month")
        .parquet(OUTPUT_PATH)
    )

    print(f"Input rows: {raw.count():,}")
    print(f"Output rows: {clean.count():,}")

    spark.stop()


if __name__ == "__main__":
    main()
