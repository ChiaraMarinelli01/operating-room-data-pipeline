"""Simple analytical report from the processed dataset."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "surgeries_clean.csv"

df = pd.read_csv(DATA)

print("\nSURGERIES BY SPECIALTY")
print(df.groupby("specialty").agg(
    surgeries=("surgery_id","count"),
    avg_duration=("duration_minutes","mean"),
    avg_waiting=("waiting_minutes","mean")
).round(1).sort_values("surgeries", ascending=False))

print("\nEMERGENCY SHARE BY HOSPITAL")
print((df.groupby("hospital")["emergency"].mean()*100).round(2))
