import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.set_page_config(page_title="OR Analytics", layout="wide")
st.title("Operating Room Analytics Dashboard")
st.caption("Portfolio project — synthetic data")

url = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://portfolio:portfolio@localhost:5432/or_analytics"
)
engine = create_engine(url)

df = pd.read_sql("SELECT * FROM surgeries", engine)
df["scheduled_date"] = pd.to_datetime(df["scheduled_date"])

c1, c2, c3, c4 = st.columns(4)
c1.metric("Surgeries", f"{len(df):,}")
c2.metric("Avg duration", f"{df.duration_minutes.mean():.0f} min")
c3.metric("Avg waiting", f"{df.waiting_minutes.mean():.0f} min")
c4.metric("Emergency rate", f"{100*df.emergency.mean():.1f}%")

st.subheader("Surgeries by specialty")
specialty = df.groupby("specialty").size().sort_values(ascending=False)
st.bar_chart(specialty)

st.subheader("Average duration by specialty")
duration = df.groupby("specialty")["duration_minutes"].mean().sort_values(ascending=False)
st.bar_chart(duration)

st.subheader("Monthly activity")
monthly = df.set_index("scheduled_date").resample("ME").size()
st.line_chart(monthly)
