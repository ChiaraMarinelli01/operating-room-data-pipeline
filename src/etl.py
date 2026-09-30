"""ETL pipeline: raw CSV -> cleaned CSV -> PostgreSQL."""

import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "surgeries_raw.csv"
PROCESSED = ROOT / "data" / "processed" / "surgeries_clean.csv"


def extract() -> pd.DataFrame:
    return pd.read_csv(RAW)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    df["scheduled_date"] = pd.to_datetime(df["scheduled_date"], errors="coerce")
    df["start_time"] = pd.to_datetime(df["start_time"], format="%H:%M", errors="coerce").dt.time

    numeric = ["duration_minutes", "waiting_minutes"]
    for c in numeric:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df["emergency"] = df["emergency"].astype(bool)
    df["outcome"] = df["outcome"].str.strip().str.title()

    df = df.drop_duplicates(subset=["surgery_id"])
    df = df.dropna(subset=["surgery_id","patient_id","specialty","hospital",
                           "room_id","scheduled_date","start_time"] + numeric)

    df = df[(df["duration_minutes"] > 0) & (df["waiting_minutes"] >= 0)]
    df["scheduled_datetime"] = pd.to_datetime(
        df["scheduled_date"].astype(str) + " " + df["start_time"].astype(str)
    )
    return df


def load_postgres(df: pd.DataFrame) -> None:
    url = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://portfolio:portfolio@localhost:5432/or_analytics"
    )
    engine = create_engine(url)

    with engine.begin() as conn:
        schema = (ROOT / "sql" / "schema.sql").read_text()
        conn.exec_driver_sql(schema)
        conn.execute(text("TRUNCATE TABLE surgeries"))

    cols = ["surgery_id","patient_id","specialty","hospital","room_id",
            "scheduled_date","start_time","duration_minutes","waiting_minutes",
            "emergency","outcome"]
    df[cols].to_sql("surgeries", engine, if_exists="append", index=False)


def main():
    df = transform(extract())
    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED, index=False)
    load_postgres(df)
    print(f"Loaded {len(df):,} rows into PostgreSQL.")


if __name__ == "__main__":
    main()
