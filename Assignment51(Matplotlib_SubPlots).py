"""
Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time. You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.

Input: months = np.arange(1, 13) 

electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) 

clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) 

home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])

 sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])
"""

import numpy as np
import matplotlib.pyplot as plt

# Data
months = np.arange(1, 13)  # Months from January to December
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot data for Electronics
axs[0, 0].plot(months, electronics_sales, marker='o', label='Electronics', color='blue')
axs[0, 0].set_title('Electronics Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales ($)')
axs[0, 0].legend()

# Plot data for Clothing
axs[0, 1].plot(months, clothing_sales, marker='o', label='Clothing', color='orange')
axs[0, 1].set_title('Clothing Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales ($)')
axs[0, 1].legend()

# Plot data for Home & Garden
axs[1, 0].plot(months, home_garden_sales, marker='o', label='Home & Garden', color='green')
axs[1, 0].set_title('Home & Garden Sales')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Sales ($)')
axs[1, 0].legend()

# Plot data for Sports & Outdoors
axs[1, 1].plot(months, sports_outdoors_sales, marker='o', label='Sports & Outdoors', color='red')
axs[1, 1].set_title('Sports & Outdoors Sales')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales ($)')
axs[1, 1].legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()

"""
*Analysis:
Electronics: The highest sales throughout the year, with a noticeable peak in December.
Clothing: Steady and moderate increase in sales each month, ending with the second-highest sales in December.
Home & Garden: Consistent growth in sales, maintaining the third-highest position throughout the year.
Sports & Outdoors: Lowest sales among the categories but showing steady growth.
*Conclusion:
Electronics had the highest sales and peaked in December. Clothing and Home & Garden showed steady growth,
with Clothing having the second-highest sales by year end. Sports & Outdoors had the lowest sales but also demonstrated consistent growth.
The focus should remain on Electronics while seeking opportunities to enhance sales in the other categories, particularly Sports & Outdoors.
"""
