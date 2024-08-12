# Lab 2: Write a Pandas program to create a Pivot table and find the item wise unit sold.


import pandas as pd

# Load the CSV file
file_path = 'C:\\Users\Aditya\Downloads\salesdata (1).csv'
sales_data = pd.read_csv(file_path)

# Creating a pivot table to find the item-wise units sold
pivot_table_units_sold = pd.pivot_table(sales_data, 
                                        values='Units', 
                                        index=['Item'], 
                                        aggfunc='sum')

# Display the pivot table
print(pivot_table_units_sold)


"""
Output:
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
"""
