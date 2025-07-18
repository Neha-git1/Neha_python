import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(42)

# Data setup
regions = ['North', 'South', 'East', 'West']
brands = ['Toyota', 'BMW', 'Hyundai', 'Ford']

data = {
    'Region': np.repeat(regions, len(brands)),
    'Brand': brands * len(regions),
    'Units Sold': np.random.randint(50, 200, size=len(regions) * len(brands))
}

df = pd.DataFrame(data)

# Group by Region
region_sales = df.groupby('Region')['Units Sold'].sum().reset_index()

# Plotting
plt.figure(figsize=(8,5))
plt.bar(region_sales['Region'], region_sales['Units Sold'], color='skyblue')
plt.title('Total Car Sales by Region')
plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
