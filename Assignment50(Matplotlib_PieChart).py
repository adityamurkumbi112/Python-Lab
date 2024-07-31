"""
Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.

 Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 

monthly_income = [5000, 1500, 1000, 600, 400]
"""

import matplotlib.pyplot as plt

# Data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightgreen', 'lightcoral', 'plum'])

# Title
plt.title('Monthly Income Distribution by Source')

# Display the chart
plt.show()

"""
*Analysis:
Salary: 62.5% of your income, showing stable primary employment.
Freelance Work: 18.8% of your income, significant secondary source.
Investments: 12.5% of your income, leveraging savings for additional income.
Rental Income: 7.5% of your income, providing passive income.
Other: 5% of your income, from minor sources.
*Conclusion:
Your income is well-diversified, with the majority coming from a stable salary and substantial contributions from 
freelance work, investments, and rental income. This diversification enhances financial stability.
"""
