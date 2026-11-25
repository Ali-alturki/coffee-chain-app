import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("cafe_sales.csv")

# Title
st.title("Qahwa Corner Sales Dashboard")

# Branch selector
branch = st.selectbox(
    "Select Branch",
    sorted(df["branch"].unique())
)

# Filter data
filtered = df[df["branch"] == branch]

# Total revenue metric
total_revenue = filtered["total_sar"].sum()

st.metric(
    "Total Revenue (SAR)",
    f"{total_revenue:,.0f}"
)

# Revenue by product
revenue_by_product = (
    filtered.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

# Bar chart
st.subheader("Revenue by Product")
st.bar_chart(revenue_by_product)