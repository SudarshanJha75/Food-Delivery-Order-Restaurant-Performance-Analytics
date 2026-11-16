from pathlib import Path
import sys
import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.analysis import get_kpis

st.set_page_config(page_title="Food Delivery Analytics", page_icon="🍽️", layout="wide")
st.title("🍽️ Food Delivery Order & Restaurant Performance Analytics")
st.caption("Bengaluru case study | Synthetic demonstration dataset — not actual platform transactions")

data_file = ROOT / "dataset" / "processed" / "cleaned_orders.csv"
if not data_file.exists():
    data_file = ROOT / "dataset" / "raw" / "bengaluru_food_delivery_sample.csv"

df = pd.read_csv(data_file)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

st.sidebar.header("Filters")
areas = st.sidebar.multiselect("Select areas", sorted(df["area"].dropna().unique()), default=sorted(df["area"].dropna().unique()))
cuisines = st.sidebar.multiselect("Select cuisines", sorted(df["cuisine"].dropna().unique()), default=sorted(df["cuisine"].dropna().unique()))
filtered = df[df["area"].isin(areas) & df["cuisine"].isin(cuisines)].copy()

if filtered.empty:
    st.warning("No records match these filters.")
    st.stop()

k = get_kpis(filtered)
c1,c2,c3,c4 = st.columns(4)
c1.metric("Total orders", f"{k['orders']:,}")
c2.metric("Delivered orders", f"{k['delivered']:,}")
c3.metric("Delivery rate", f"{k['delivery_rate']:.1f}%")
c4.metric("Average delivery", f"{k['avg_delivery_time']:.1f} min")

c5,c6 = st.columns(2)
c5.metric("Food revenue", f"₹{k['food_revenue']:,.0f}")
c6.metric("Average order value", f"₹{k['avg_order_value']:,.0f}")

st.subheader("Order trends")
hourly = filtered.groupby("order_hour", as_index=False)["order_id"].count()
st.plotly_chart(px.bar(hourly, x="order_hour", y="order_id", labels={"order_hour":"Hour","order_id":"Orders"}), use_container_width=True)

left,right = st.columns(2)
with left:
    area_rev = filtered.groupby("area", as_index=False)["food_revenue"].sum().sort_values("food_revenue", ascending=False)
    st.plotly_chart(px.bar(area_rev, x="area", y="food_revenue", title="Food revenue by area"), use_container_width=True)
with right:
    traffic = filtered.groupby("traffic", as_index=False)["delivery_time_min"].mean()
    st.plotly_chart(px.bar(traffic, x="traffic", y="delivery_time_min", title="Average delivery time by traffic"), use_container_width=True)

st.subheader("Restaurant performance")
restaurants = filtered.groupby("restaurant_name", as_index=False).agg(
    orders=("order_id","count"),
    revenue=("food_revenue","sum"),
    avg_rating=("restaurant_rating","mean")
).sort_values("revenue", ascending=False)
st.dataframe(restaurants, use_container_width=True)

st.subheader("Filtered order records")
st.dataframe(filtered.head(100), use_container_width=True)
