import pandas as pd

# Sample data: car sales by region
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Car Brand': ['Toyota', 'Toyota', 'Ford', 'Ford', 'BMW', 'BMW', 'Hyundai', 'Hyundai'],
    'Units Sold': [120, 150, 100, 130, 90, 110, 105, 115]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print("Car Sales Data:")
print(df)

# Group by region and summarize total units sold
grouped = df.groupby('Region')['Units Sold'].sum().reset_index()

print("\nTotal Units Sold by Region:")
print(grouped)

# Pivot table (optional, for a more matrix-style view)
pivot = df.pivot_table(values='Units Sold', index='Region', columns='Car Brand', aggfunc='sum', fill_value=0)

print("\nPivot Table (Car Brand Sales per Region):")
print(pivot)
