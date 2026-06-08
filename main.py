"""
=============================================================
  Exploratory Data Analysis (EDA) Project
  main.py — Run the full EDA pipeline in one command
=============================================================
  Usage: python main.py
"""

import sys, os, subprocess

def run(script, label):
    print(f"\n{'='*60}\n  ▶  {label}\n{'='*60}")
    r = subprocess.run([sys.executable, script])
    if r.returncode != 0:
        print(f"❌ Failed: {label}")
        sys.exit(1)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("\n🚀 Starting EDA Pipeline: Retail Sales Analysis\n")
    run("scripts/statistical_summary.py", "Step 1 — Statistical Summary")
    run("scripts/eda_visualizations.py",  "Step 2 — Visualizations (8 Charts)")
    run("scripts/generate_report.py",     "Step 3 — Structured Insights Report")
    print("\n🎉 EDA PIPELINE COMPLETE!")
    print("📁 All outputs saved in 'outputs/' folder:")
    print("   • statistical_summary.txt")
    print("   • eda_report.txt")
    print("   • chart1_monthly_trend.png")
    print("   • chart2_category_breakdown.png")
    print("   • chart3_heatmap_region_category.png")
    print("   • chart4_discount_vs_profit.png")
    print("   • chart5_top_subcategories.png")
    print("   • chart6_customer_segments.png")
    print("   • chart7_correlation_heatmap.png")
    print("   • chart8_shipping_analysis.png\n")
