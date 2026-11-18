import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cafe_sales.csv")

st.title("Coffee Chain Dashboard")

branch = st.selectbox(
    "Select Branch",
    sorted(df["branch"].unique())
)

filtered_df = df[df["branch"] == branch]

total_revenue = filtered_df["total_sar"].sum()

st.metric(
    "Total Revenue (SAR)",
    f"{total_revenue:,.2f}"
)

revenue_by_product = (
    filtered_df.groupby("product")["total_sar"]
    .sum()
    .reset_index()
)

fig = px.bar(
    revenue_by_product,
    x="product",
    y="total_sar",
    title="Revenue by Product"
)

st.plotly_chart(fig, use_container_width=True)
