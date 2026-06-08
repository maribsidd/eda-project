# 🔍 Exploratory Data Analysis (EDA) Project


---

## 📌 Project Overview

This project performs a **full Exploratory Data Analysis** on a retail sales dataset covering **100 orders** across 7 months (Jan–Jul 2024). The goal is to uncover patterns, trends, and actionable insights using statistical summaries and visualizations.

**Dataset:** Retail sales transactions across Technology, Furniture, and Office Supplies categories, sold across 4 US regions (East, West, South, North).

---

## 🗂️ Project Structure

```
eda_project/
│
├── data/
│   └── retail_sales.csv           # Raw dataset (100 orders, 16 features)
│
├── scripts/
│   ├── statistical_summary.py     # Step 1: Stats, groupby, correlations
│   ├── eda_visualizations.py      # Step 2: 8 insightful charts
│   └── generate_report.py         # Step 3: Auto-generate text report
│
├── outputs/                       # Auto-generated after running
│   ├── statistical_summary.txt
│   ├── eda_report.txt
│   ├── chart1_monthly_trend.png
│   ├── chart2_category_breakdown.png
│   ├── chart3_heatmap_region_category.png
│   ├── chart4_discount_vs_profit.png
│   ├── chart5_top_subcategories.png
│   ├── chart6_customer_segments.png
│   ├── chart7_correlation_heatmap.png
│   └── chart8_shipping_analysis.png
│
├── main.py                        # ▶ Run the full pipeline
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/eda-project.git
cd eda-project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full EDA pipeline
python main.py
```

---

## 📊 What Gets Analyzed

### Step 1 — Statistical Summary
- Shape, data types, missing values check
- Descriptive stats (mean, median, std, min, max)
- Group-by analysis: Category, Region, Customer Segment
- Correlation matrix for numerical features

### Step 2 — 8 Visualizations

| # | Chart | Insight |
|---|-------|---------|
| 1 | Monthly Sales & Profit Trend | Revenue growth over time |
| 2 | Category Sales Pie + Bar | Which category dominates? |
| 3 | Category × Region Heatmap | Where is each category sold most? |
| 4 | Discount vs Profit Scatter | Do discounts hurt margins? |
| 5 | Top Sub-Categories by Revenue | Best-performing product lines |
| 6 | Customer Segment Deep-Dive | Who orders most and who's profitable? |
| 7 | Correlation Heatmap | Feature relationships |
| 8 | Shipping Mode Analysis | Cost vs profit by delivery type |

### Step 3 — Structured Insights Report
Auto-generated `eda_report.txt` with 10 sections covering:
- Executive Summary
- Revenue & Profitability breakdown
- Regional & Segment analysis
- Discount impact quantification
- Key Findings & Recommendations

---

## 💡 Key Findings (Sample)

- **Technology** is the top revenue and profit category
- **Discounts ≥ 10%** significantly reduce per-order profit
- **West region** leads in total sales volume
- **Corporate customers** generate the highest total profit
- Strong **positive correlation** between Sales and Profit (r ≈ 0.95)
- **Negative correlation** between Discount and Profit (discounts hurt margins)

---

## 📚 Libraries Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, groupby, aggregations |
| `numpy` | Numerical calculations |
| `matplotlib` | Plotting engine |
| `seaborn` | Heatmaps, statistical charts |

---

## 📈 Dataset Features

| Column | Description |
|--------|-------------|
| OrderID | Unique order identifier |
| Date | Order date |
| Category | Technology / Furniture / Office Supplies |
| SubCategory | Product sub-type |
| Product | Product name |
| Region | East / West / South / North |
| State / City | Location details |
| CustomerSegment | Consumer / Corporate / Home Office |
| Sales | Order revenue (USD) |
| Quantity | Units ordered |
| Discount | Discount applied (0.0–1.0) |
| Profit | Net profit (USD) |
| ShippingCost | Delivery cost (USD) |
| ShipMode | Standard / Second / First / Same Day |

---

## 👤 Author

**Mohd Marib**
