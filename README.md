# 🛒 Retail Sales Analysis & Price Prediction

A full-stack Python application that turns raw retail transaction data (2022–2025) into actionable insights and ML-powered unit price predictions.

---

## 📁 Project Structure

```
retail_analytics/
├── app.py                        # Streamlit entry point (home page)
├── requirements.txt              # Python dependencies
├── data/
│   └── Sales_transactions_2022_2025.csv
├── models/
│   └── price_model.joblib        # Auto-generated after first run
├── pages/
│   ├── 1_Dashboard.py            # Executive KPI overview
│   ├── 2_EDA.py                  # Exploratory data analysis
│   └── 3_Price_Prediction.py     # ML prediction UI
└── src/
    ├── __init__.py
    ├── data_loader.py            # Load, clean, feature-engineer CSV
    ├── analytics.py              # Plotly chart helpers
    └── model.py                  # GradientBoosting ML pipeline
```

---

## 🚀 Quick Start

### 1. Install Python
Download from https://www.python.org/downloads/ (3.9+ recommended).

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
cd retail_analytics
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---

## 📊 Pages

### Home (`app.py`)
- Dataset summary and navigation guide

### Dashboard (`pages/1_Dashboard.py`)
- 8 KPI metric tiles: revenue, profit, margin, orders, return rate, rating, customers, avg order value
- Monthly revenue trend line chart
- Year-over-Year comparison
- Revenue by category (bar), channel (donut), country (horizontal bar)
- Profit margin by category
- Global sidebar filters: year, category, country, channel

### EDA (`pages/2_EDA.py`)
Five tabs:
| Tab | Charts |
|---|---|
| 🛍️ Products | Top N products, subcategory treemap, category summary table |
| 👥 Customers | Segment revenue, age histogram, rating distribution, payment methods |
| ↩️ Returns | Return rate by category + country, return reasons |
| 💰 Pricing | Profit vs discount scatter, avg price by category, discount distribution, shipping days |
| 📅 Temporal | Revenue heatmap (day × month), quarterly revenue bar |

### Price Prediction (`pages/3_Price_Prediction.py`)
- Auto-trains a **GradientBoostingRegressor** on first load (~20s)
- Model metrics: R², MAE, RMSE
- Feature importance horizontal bar chart
- **Interactive prediction form**: select category, subcategory, quantity, discount, channel, segment, country, month, promotion → get predicted unit price + estimated sales amount
- Similar historical transactions table
- Actual vs Predicted scatter plot (500 test-set samples)
- Residuals distribution histogram
- Re-train button

---

## 🧠 ML Model Details

| Item | Detail |
|---|---|
| **Target** | `Unit_Price` |
| **Algorithm** | GradientBoostingRegressor (sklearn) |
| **Features** | Product_Category, Product_Subcategory, Quantity, Discount_Percentage, Sales_Channel, Customer_Segment, Country, Order_Month, Order_Quarter, Has_Promotion |
| **Preprocessing** | OrdinalEncoder for categoricals, MedianImputer for numerics |
| **Train/Test Split** | 80/20, `random_state=42` |
| **Hyperparams** | n_estimators=300, max_depth=5, learning_rate=0.08, subsample=0.8 |
| **Persistence** | `models/price_model.joblib` (auto-created, re-used on reload) |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Frontend / UI |
| `pandas` | Data manipulation |
| `numpy` | Numeric operations |
| `scikit-learn` | ML pipeline & model |
| `plotly` | Interactive charts |
| `joblib` | Model serialization |
