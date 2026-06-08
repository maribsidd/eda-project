"""
=============================================================
  Exploratory Data Analysis (EDA) Project
  Script 1: statistical_summary.py
  Purpose : Load data and generate full statistical profile
=============================================================
"""

import pandas as pd
import numpy as np
import os

def summarize():
    print("=" * 60)
    print("  STEP 1: Statistical Summary")
    print("=" * 60)

    df = pd.read_csv("data/retail_sales.csv", parse_dates=["Date"])
    print(f"✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")

    # ── Basic Info ────────────────────────────────────────────
    print("\n📋 DATASET OVERVIEW")
    print(f"   Date Range  : {df['Date'].min().date()} → {df['Date'].max().date()}")
    print(f"   Total Orders: {len(df)}")
    print(f"   Total Sales : ${df['Sales'].sum():,.2f}")
    print(f"   Total Profit: ${df['Profit'].sum():,.2f}")
    print(f"   Avg Discount: {df['Discount'].mean()*100:.1f}%")
    print(f"   Profit Margin: {(df['Profit'].sum()/df['Sales'].sum())*100:.1f}%")

    # ── Numeric Stats ─────────────────────────────────────────
    print("\n📊 NUMERICAL STATISTICS")
    numeric_cols = ["Sales", "Quantity", "Discount", "Profit", "ShippingCost"]
    stats = df[numeric_cols].describe().round(2)
    print(stats.to_string())

    # ── Categorical Breakdown ─────────────────────────────────
    print("\n🗂️  CATEGORICAL BREAKDOWN")
    for col in ["Category", "Region", "CustomerSegment", "ShipMode"]:
        print(f"\n  {col}:")
        vc = df[col].value_counts()
        for val, cnt in vc.items():
            pct = cnt / len(df) * 100
            print(f"    {val:<25} {cnt:>4} orders  ({pct:.1f}%)")

    # ── Profitability by Category ─────────────────────────────
    print("\n💰 PROFITABILITY BY CATEGORY")
    cat_stats = df.groupby("Category").agg(
        Orders=("OrderID", "count"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Avg_Discount=("Discount", "mean")
    ).round(2)
    cat_stats["Margin_%"] = (cat_stats["Total_Profit"] / cat_stats["Total_Sales"] * 100).round(1)
    print(cat_stats.to_string())

    # ── Region Performance ────────────────────────────────────
    print("\n🗺️  REGIONAL PERFORMANCE")
    reg_stats = df.groupby("Region").agg(
        Orders=("OrderID", "count"),
        Revenue=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).sort_values("Revenue", ascending=False).round(2)
    print(reg_stats.to_string())

    # ── Correlation Matrix ────────────────────────────────────
    print("\n🔗 KEY CORRELATIONS")
    corr = df[numeric_cols].corr().round(3)
    print(corr.to_string())

    # Save summary to text file
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/statistical_summary.txt", "w") as f:
        f.write("EDA PROJECT — STATISTICAL SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Date Range   : {df['Date'].min().date()} to {df['Date'].max().date()}\n")
        f.write(f"Total Orders : {len(df)}\n")
        f.write(f"Total Sales  : ${df['Sales'].sum():,.2f}\n")
        f.write(f"Total Profit : ${df['Profit'].sum():,.2f}\n")
        f.write(f"Profit Margin: {(df['Profit'].sum()/df['Sales'].sum())*100:.1f}%\n\n")
        f.write("NUMERICAL STATISTICS\n" + "-"*40 + "\n")
        f.write(stats.to_string() + "\n\n")
        f.write("PROFITABILITY BY CATEGORY\n" + "-"*40 + "\n")
        f.write(cat_stats.to_string() + "\n\n")
        f.write("REGIONAL PERFORMANCE\n" + "-"*40 + "\n")
        f.write(reg_stats.to_string() + "\n\n")
        f.write("CORRELATION MATRIX\n" + "-"*40 + "\n")
        f.write(corr.to_string() + "\n")

    print("\n💾 Summary saved → outputs/statistical_summary.txt")
    print("✅ Statistical Summary Complete!\n")
    return df

if __name__ == "__main__":
    summarize()
