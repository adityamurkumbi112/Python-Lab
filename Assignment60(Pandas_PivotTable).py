#Lab 1: Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd

# Load the CSV file
file_path = 'C:\\Users\Aditya\Downloads\salesdata (1).csv'
sales_data = pd.read_csv(file_path)

# Creating a pivot table to find the total sale amount region-wise, manager-wise, and salesman-wise
pivot_table = pd.pivot_table(sales_data, 
                             values='Sale_amt', 
                             index=['Region', 'Manager', 'SalesMan'], 
                             aggfunc='sum')

# Display the pivot table
print(pivot_table)



"""
Output:
                           Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0
"""
