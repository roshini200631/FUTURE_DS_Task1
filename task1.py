import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

# Load dataset
df = load_data("sales_data.csv")

# -----------------------------
# 1. Revenue Trend (Monthly)
# -----------------------------
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o')
plt.title("Monthly Sales Trend")
plt.show()

# -----------------------------
# 2. Top Selling Products
# -----------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
top_products.plot(kind='barh')
plt.title("Top 10 Products by Sales")
plt.gca().invert_yaxis()
plt.show()

# -----------------------------
# 3. Category Performance
# -----------------------------
category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Sales by Category")
plt.ylabel("")
plt.show()

# -----------------------------
# 4. Regional Performance
# -----------------------------
region_sales = df.groupby('Region')['Sales'].sum().sort_values()

region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.show()

# -----------------------------
# 5. Profit Analysis
# -----------------------------
profit_trend = df.groupby('Year')['Profit'].sum()

profit_trend.plot(kind='bar')
plt.title("Yearly Profit")
plt.show()
