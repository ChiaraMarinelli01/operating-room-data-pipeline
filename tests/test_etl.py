import pandas as pd

from src.etl import transform


def make_sample_data():
    return pd.DataFrame({
        "surgery_id": ["S1", "S1", "S2", "S3"],
        "patient_id": ["P1", "P1", "P2", "P3"],
        "specialty": ["ENT", "ENT", "Urology", "Cardiology"],
        "hospital": ["A", "A", "B", "C"],
        "room_id": ["OR01", "OR01", "OR02", "OR03"],
        "scheduled_date": [
            "2025-01-01",
            "2025-01-01",
            "2025-01-02",
            "2025-01-03"
        ],
        "start_time": ["08:00", "08:00", "09:30", "10:00"],
        "duration_minutes": [60, 60, -5, 90],
        "waiting_minutes": [10, 10, 5, -1],
        "emergency": [0, 0, 1, 0],
        "outcome": ["Completed", "Completed", "Completed", "Cancelled"]
    })


def test_transform_removes_duplicates_and_invalid_rows():
    result = transform(make_sample_data())

    assert len(result) == 1
    assert result.iloc[0]["surgery_id"] == "S1"


def test_transform_converts_dates_and_times():
    result = transform(make_sample_data())

    row = result.iloc[0]

    assert pd.notna(row["scheduled_date"])
    assert row["start_time"].strftime("%H:%M") == "08:00"
    assert row["scheduled_datetime"] == pd.Timestamp("2025-01-01 08:00:00")


def test_transform_converts_emergency_to_boolean():
    result = transform(make_sample_data())

    assert result["emergency"].dtype == bool
    assert not result.iloc[0]["emergency"]
