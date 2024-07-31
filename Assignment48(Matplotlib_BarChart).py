"""
Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

expenses = [1200, 400, 200, 150, 250]
"""
import matplotlib.pyplot as plt

# Categories for the expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']

# Monthly expenses in dollars for each category
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.bar(categories, expenses)

# Add x-axis label
# This describes what each bar represents
plt.xlabel('Category')

# Add y-axis label
# This shows the unit of measurement for the expenses
plt.ylabel('Expenses ($)')

# Add a title to the chart
# This provides context to what the chart is about
plt.title('Monthly Expenses by Category')

# Display the bar chart
# This renders the chart and makes it visible
plt.show()

"""
Conclusion:
From this bar chart, you can easily compare your spending in different categories. For example:

Rent is the largest expense, followed by Groceries.
Entertainment has the smallest expense.
Utilities and Transportation have moderate expenses.
"""
