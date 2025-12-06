"""
E-commerce Customer Retention Analysis
Student Email: 23f2005282@ds.study.iitm.ac.in
Created using LLM assistance (Claude AI)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Set style for professional visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 70)
print("E-COMMERCE CUSTOMER RETENTION ANALYSIS")
print("=" * 70)
print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"Analyst Email: 23f2005282@ds.study.iitm.ac.in")
print("=" * 70)

# Customer Retention Rate - 2024 Quarterly Data
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Retention_Rate': [72.4, 69.46, 75.72, 71.75],
    'Quarter_Num': [1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Calculate key metrics
average_retention = df['Retention_Rate'].mean()
industry_target = 85
gap_to_target = industry_target - average_retention
min_retention = df['Retention_Rate'].min()
max_retention = df['Retention_Rate'].max()
volatility = df['Retention_Rate'].std()

print("\n📊 KEY METRICS")
print("-" * 70)
print(f"Average Retention Rate: {average_retention:.2f}%")
print(f"Industry Target: {industry_target}%")
print(f"Gap to Target: {gap_to_target:.2f} percentage points")
print(f"Minimum (Q2): {min_retention}%")
print(f"Maximum (Q3): {max_retention}%")
print(f"Standard Deviation: {volatility:.2f}%")
print(f"Performance vs Target: {(average_retention/industry_target)*100:.1f}%")

# Quarterly comparison
print("\n📈 QUARTERLY PERFORMANCE")
print("-" * 70)
for idx, row in df.iterrows():
    trend = "📈" if idx > 0 and row['Retention_Rate'] > df.iloc[idx-1]['Retention_Rate'] else "📉" if idx > 0 else "➡️"
    gap = industry_target - row['Retention_Rate']
    print(f"{row['Quarter']}: {row['Retention_Rate']}% {trend} (Gap: {gap:.2f}pp)")

# Create comprehensive visualizations
fig = plt.figure(figsize=(16, 10))

# 1. Trend Line Chart with Target
ax1 = plt.subplot(2, 2, 1)
plt.plot(df['Quarter'], df['Retention_Rate'], marker='o', linewidth=3, 
         markersize=10, label='Actual Retention', color='#e74c3c')
plt.axhline(y=industry_target, color='#27ae60', linestyle='--', 
            linewidth=2, label='Industry Target (85%)')
plt.axhline(y=average_retention, color='#3498db', linestyle=':', 
            linewidth=2, label=f'Average ({average_retention:.2f}%)')
plt.fill_between(df['Quarter'], df['Retention_Rate'], industry_target, 
                  alpha=0.2, color='red')
plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('Retention Rate (%)', fontsize=12, fontweight='bold')
plt.title('Customer Retention Trend vs Industry Target', fontsize=14, fontweight='bold', pad=15)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
for i, row in df.iterrows():
    plt.text(i, row['Retention_Rate'] + 1, f"{row['Retention_Rate']}%", 
             ha='center', fontweight='bold')

# 2. Gap Analysis Bar Chart
ax2 = plt.subplot(2, 2, 2)
gaps = industry_target - df['Retention_Rate']
colors_gap = ['#e74c3c' if gap > 0 else '#27ae60' for gap in gaps]
bars = plt.bar(df['Quarter'], gaps, color=colors_gap, alpha=0.7, edgecolor='black')
plt.axhline(y=0, color='black', linewidth=1)
plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('Gap to Target (pp)', fontsize=12, fontweight='bold')
plt.title('Gap to Industry Target by Quarter', fontsize=14, fontweight='bold', pad=15)
plt.grid(True, alpha=0.3, axis='y')
for i, (bar, gap) in enumerate(zip(bars, gaps)):
    plt.text(i, gap + 0.5, f"{gap:.2f}pp", ha='center', fontweight='bold')

# 3. Performance Distribution
ax3 = plt.subplot(2, 2, 3)
categories = ['Current\nAverage\n(72.33%)', 'Industry\nTarget\n(85%)']
values = [average_retention, industry_target]
colors_perf = ['#e74c3c', '#27ae60']
bars = plt.bar(categories, values, color=colors_perf, alpha=0.7, edgecolor='black', linewidth=2)
plt.ylabel('Retention Rate (%)', fontsize=12, fontweight='bold')
plt.title('Current Performance vs Industry Benchmark', fontsize=14, fontweight='bold', pad=15)
plt.ylim(0, 100)
for bar, val in zip(bars, values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{val:.2f}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
# Add gap annotation
plt.annotate('', xy=(0.5, average_retention), xytext=(0.5, industry_target),
             arrowprops=dict(arrowstyle='<->', color='black', lw=2))
plt.text(0.5, (average_retention + industry_target)/2, f'Gap:\n{gap_to_target:.2f}pp',
         ha='center', fontweight='bold', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# 4. Quarterly Variance Analysis
ax4 = plt.subplot(2, 2, 4)
mean_line = [average_retention] * len(df)
plt.bar(df['Quarter'], df['Retention_Rate'], alpha=0.6, color='#3498db', 
        edgecolor='black', label='Actual')
plt.plot(df['Quarter'], mean_line, color='#e74c3c', linewidth=2, 
         linestyle='--', label=f'Average ({average_retention:.2f}%)')
plt.xlabel('Quarter', fontsize=12, fontweight='bold')
plt.ylabel('Retention Rate (%)', fontsize=12, fontweight='bold')
plt.title('Quarterly Variance from Average', fontsize=14, fontweight='bold', pad=15)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('customer_retention_analysis.png', dpi=300, bbox_inches='tight')
print("\n✅ Visualization saved as 'customer_retention_analysis.png'")

# Statistical Analysis
print("\n📊 STATISTICAL INSIGHTS")
print("-" * 70)

# Trend analysis
q_over_q_changes = df['Retention_Rate'].diff()
print("\nQuarter-over-Quarter Changes:")
for i in range(1, len(df)):
    change = q_over_q_changes.iloc[i]
    direction = "increase" if change > 0 else "decrease"
    print(f"  Q{i} to Q{i+1}: {abs(change):.2f}pp {direction}")

# Identify problem quarters
below_average = df[df['Retention_Rate'] < average_retention]
print(f"\n⚠️ Quarters Below Average: {len(below_average)} out of 4")
for _, row in below_average.iterrows():
    print(f"  {row['Quarter']}: {row['Retention_Rate']}%")

# Calculate improvement needed
print("\n🎯 IMPROVEMENT TARGETS")
print("-" * 70)
for _, row in df.iterrows():
    needed = industry_target - row['Retention_Rate']
    improvement_pct = (needed / row['Retention_Rate']) * 100
    print(f"{row['Quarter']}: Need {needed:.2f}pp improvement ({improvement_pct:.1f}% increase)")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
print(f"\n💡 CRITICAL FINDING: Average retention of {average_retention:.2f}% is")
print(f"   {gap_to_target:.2f} percentage points below the industry target of {industry_target}%")
print(f"\n📧 Contact: 23f2005282@ds.study.iitm.ac.in")
print("=" * 70)

plt.show()
