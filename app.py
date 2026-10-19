"""
app.py – Streamlit entry point for Retail Sales Analysis & Price Prediction.

Run with:
    streamlit run app.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

st.set_page_config(
    page_title="Retail Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Landing page ───────────────────────────────────────────────────────────
st.title("🛒 Retail Sales Analysis & Price Prediction")
st.markdown(
    """
    Welcome to the **Retail Analytics Platform** — a full-stack Python application that
    turns raw sales transactions into actionable insights and ML-powered price predictions.
    """
)

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        ### 📊 Dashboard
        Executive KPI overview:
        - Total revenue, profit, and margins
        - Revenue trend (monthly & year-over-year)
        - Breakdown by category, country, and channel

        👉 Open **Dashboard** from the sidebar.
        """
    )

with c2:
    st.markdown(
        """
        ### 🔬 EDA
        Deep-dive exploratory analysis:
        - Top products & subcategory treemap
        - Customer demographics & ratings
        - Return rates and reasons
        - Pricing, discount, and temporal heatmaps

        👉 Open **EDA** from the sidebar.
        """
    )

with c3:
    st.markdown(
        """
        ### 🤖 Price Prediction
        ML-powered unit price estimator:
        - GradientBoosting model (scikit-learn)
        - Feature importance chart
        - Interactive prediction form
        - Actual vs Predicted scatter & residuals

        👉 Open **Price Prediction** from the sidebar.
        """
    )

st.divider()

# ── Dataset snapshot ───────────────────────────────────────────────────────
st.subheader("📂 Dataset Snapshot")
from src.data_loader import load_data, get_kpis

df = load_data()
kpis = get_kpis(df)

k1, k2, k3, k4 = st.columns(4)
k1.metric("Transactions", f"{len(df):,}")
k2.metric("Unique Products", f"{df['Product_ID'].nunique():,}")
k3.metric("Date Range", f"{df['Order_Date'].min().date()} → {df['Order_Date'].max().date()}")
k4.metric("Countries", f"{df['Country'].nunique():,}")

st.markdown(
    f"""
    | Feature | Value |
    |---|---|
    | Columns | {df.shape[1]} |
    | Product Categories | {', '.join(sorted(df['Product_Category'].dropna().unique().tolist()))} |
    | Sales Channels | {', '.join(sorted(df['Sales_Channel'].dropna().unique().tolist()))} |
    | Year Range | {int(df['Order_Year'].min())} – {int(df['Order_Year'].max())} |
    """
)

st.info("Use the **sidebar** to navigate between pages.", icon="⬅️")
