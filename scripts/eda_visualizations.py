"""
=============================================================
  Exploratory Data Analysis (EDA) Project
  Script 2: eda_visualizations.py
  Purpose : Generate 8 insightful EDA charts
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 130
os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/retail_sales.csv", parse_dates=["Date"])
df["Month"]         = df["Date"].dt.to_period("M").astype(str)
df["MonthNum"]      = df["Date"].dt.month
df["ProfitMargin"]  = (df["Profit"] / df["Sales"] * 100).round(2)

print("=" * 60)
print("  Generating EDA Visualizations")
print("=" * 60)

# ── CHART 1: Monthly Sales & Profit Trend ─────────────────────
print("\n📊 Chart 1: Monthly Sales & Profit Trend")
monthly = df.groupby("Month")[["Sales", "Profit"]].sum().reset_index()

fig, ax1 = plt.subplots(figsize=(13, 5))
ax2 = ax1.twinx()
x = range(len(monthly))
bars = ax1.bar(x, monthly["Sales"], color="#2196F3", alpha=0.7, label="Sales", width=0.6)
ax2.plot(x, monthly["Profit"], "o-", color="#FF5722", lw=2.5, ms=7, label="Profit", zorder=5)
ax1.set_xticks(x)
ax1.set_xticklabels(monthly["Month"], rotation=45, ha="right", fontsize=9)
ax1.set_ylabel("Total Sales (USD)", fontsize=12, color="#2196F3")
ax2.set_ylabel("Total Profit (USD)", fontsize=12, color="#FF5722")
ax1.yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax2.yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax1.set_title("Monthly Sales & Profit Trend (Jan–Jul 2024)", fontsize=15, fontweight="bold")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=11)
plt.tight_layout()
plt.savefig("outputs/chart1_monthly_trend.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart1_monthly_trend.png")

# ── CHART 2: Sales by Category (Pie + Bar side by side) ───────
print("📊 Chart 2: Sales Distribution by Category")
cat_sales   = df.groupby("Category")["Sales"].sum()
cat_profit  = df.groupby("Category")["Profit"].sum()
cat_colors  = ["#FF6B6B", "#4ECDC4", "#45B7D1"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
wedges, texts, autotexts = ax1.pie(
    cat_sales, labels=cat_sales.index, autopct="%1.1f%%",
    colors=cat_colors, startangle=140,
    wedgeprops=dict(edgecolor="white", linewidth=2), textprops={"fontsize": 12}
)
for at in autotexts: at.set_fontweight("bold")
ax1.set_title("Sales Share by Category", fontsize=13, fontweight="bold")

x = np.arange(len(cat_sales))
b1 = ax2.bar(x - 0.2, cat_sales.values, 0.35, label="Sales", color=cat_colors, alpha=0.85, edgecolor="white")
b2 = ax2.bar(x + 0.2, cat_profit.values, 0.35, label="Profit", color=cat_colors, alpha=0.45, edgecolor="white", hatch="//")
ax2.set_xticks(x); ax2.set_xticklabels(cat_sales.index, fontsize=11)
ax2.set_ylabel("USD", fontsize=12)
ax2.yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax2.set_title("Sales vs Profit by Category", fontsize=13, fontweight="bold")
ax2.legend(fontsize=11)
for bar in b1:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f"${bar.get_height():,.0f}", ha="center", fontsize=9, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/chart2_category_breakdown.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart2_category_breakdown.png")

# ── CHART 3: Regional Sales Heatmap ───────────────────────────
print("📊 Chart 3: Category × Region Heatmap")
pivot = df.pivot_table(values="Sales", index="Category",
                       columns="Region", aggfunc="sum").fillna(0)
fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(pivot, annot=True, fmt=",.0f", cmap="YlOrRd",
            linewidths=0.5, ax=ax, cbar_kws={"label": "Sales (USD)"})
ax.set_title("Sales Heatmap: Category × Region", fontsize=15, fontweight="bold")
ax.set_xlabel("Region", fontsize=12); ax.set_ylabel("Category", fontsize=12)
plt.tight_layout()
plt.savefig("outputs/chart3_heatmap_region_category.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart3_heatmap_region_category.png")

# ── CHART 4: Discount vs Profit Scatter ───────────────────────
print("📊 Chart 4: Discount vs Profit Scatter")
fig, ax = plt.subplots(figsize=(9, 6))
categories = df["Category"].unique()
palette = {"Technology": "#2196F3", "Furniture": "#FF5722", "Office Supplies": "#4CAF50"}
for cat in categories:
    sub = df[df["Category"] == cat]
    ax.scatter(sub["Discount"] * 100, sub["Profit"],
               label=cat, color=palette[cat], alpha=0.65, s=70, edgecolors="white", lw=0.5)
z = np.polyfit(df["Discount"] * 100, df["Profit"], 1)
p = np.poly1d(z)
x_line = np.linspace(0, 25, 100)
ax.plot(x_line, p(x_line), "k--", lw=1.8, label="Trend Line", alpha=0.7)
ax.set_xlabel("Discount (%)", fontsize=12)
ax.set_ylabel("Profit (USD)", fontsize=12)
ax.set_title("Discount vs Profit — Are Discounts Hurting Margins?", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
ax.axhline(0, color="red", lw=1, linestyle=":", alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/chart4_discount_vs_profit.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart4_discount_vs_profit.png")

# ── CHART 5: Top 10 Sub-Categories by Revenue ─────────────────
print("📊 Chart 5: Top Sub-Categories by Revenue")
sub_rev = df.groupby("SubCategory")["Sales"].sum().sort_values(ascending=True).tail(10)
fig, ax = plt.subplots(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0.3, 0.85, len(sub_rev)))
bars = ax.barh(sub_rev.index, sub_rev.values, color=colors, edgecolor="white")
for bar in bars:
    ax.text(bar.get_width() + 300, bar.get_y() + bar.get_height()/2,
            f"${bar.get_width():,.0f}", va="center", fontsize=10)
ax.set_xlabel("Total Sales (USD)", fontsize=12)
ax.set_title("Top Sub-Categories by Total Revenue", fontsize=15, fontweight="bold")
ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
plt.tight_layout()
plt.savefig("outputs/chart5_top_subcategories.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart5_top_subcategories.png")

# ── CHART 6: Customer Segment Analysis ────────────────────────
print("📊 Chart 6: Customer Segment Deep-Dive")
seg = df.groupby("CustomerSegment").agg(
    Orders=("OrderID", "count"),
    Revenue=("Sales", "sum"),
    Profit=("Profit", "sum"),
    AvgOrderValue=("Sales", "mean")
).reset_index()

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Customer Segment Analysis", fontsize=15, fontweight="bold")
seg_colors = ["#3F51B5", "#E91E63", "#009688", "#FF9800"]

axes[0].pie(seg["Orders"], labels=seg["CustomerSegment"], autopct="%1.0f%%",
            colors=seg_colors[:len(seg)], wedgeprops=dict(edgecolor="white", lw=2))
axes[0].set_title("Order Share", fontsize=12, fontweight="bold")

axes[1].bar(seg["CustomerSegment"], seg["Revenue"], color=seg_colors[:len(seg)], edgecolor="white")
axes[1].set_title("Total Revenue", fontsize=12, fontweight="bold")
axes[1].yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
axes[1].tick_params(axis="x", rotation=15)

axes[2].bar(seg["CustomerSegment"], seg["AvgOrderValue"], color=seg_colors[:len(seg)], edgecolor="white")
axes[2].set_title("Avg Order Value", fontsize=12, fontweight="bold")
axes[2].yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, _: f"${v:,.0f}"))
axes[2].tick_params(axis="x", rotation=15)

plt.tight_layout()
plt.savefig("outputs/chart6_customer_segments.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart6_customer_segments.png")

# ── CHART 7: Correlation Heatmap ──────────────────────────────
print("📊 Chart 7: Correlation Heatmap")
num_df = df[["Sales", "Quantity", "Discount", "Profit", "ShippingCost", "ProfitMargin"]]
corr = num_df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, vmin=-1, vmax=1, linewidths=0.5, ax=ax,
            mask=mask, annot_kws={"size": 11})
ax.set_title("Correlation Matrix — Numerical Features", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/chart7_correlation_heatmap.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart7_correlation_heatmap.png")

# ── CHART 8: Shipping Mode vs Avg Delivery Cost & Profit ──────
print("📊 Chart 8: Shipping Mode Analysis")
ship = df.groupby("ShipMode").agg(
    Orders=("OrderID", "count"),
    AvgShipCost=("ShippingCost", "mean"),
    AvgProfit=("Profit", "mean"),
    TotalRevenue=("Sales", "sum")
).reset_index().sort_values("AvgProfit", ascending=False)

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(ship))
w = 0.35
b1 = ax.bar(x - w/2, ship["AvgShipCost"], w, label="Avg Shipping Cost", color="#607D8B", edgecolor="white")
b2 = ax.bar(x + w/2, ship["AvgProfit"],   w, label="Avg Profit",        color="#8BC34A", edgecolor="white")
for bar in list(b1) + list(b2):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"${bar.get_height():.0f}", ha="center", fontsize=10, fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(ship["ShipMode"], fontsize=11)
ax.set_ylabel("USD", fontsize=12)
ax.set_title("Shipping Mode: Cost vs Profit Analysis", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("outputs/chart8_shipping_analysis.png", bbox_inches="tight")
plt.close()
print("   ✅ Saved → outputs/chart8_shipping_analysis.png")

print("\n" + "=" * 60)
print("  ✅ All 8 Charts Generated! → outputs/ folder")
print("=" * 60)
