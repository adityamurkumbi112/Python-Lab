"""
Visualize the daily temperature changes over time in a city and give your conclusion

 Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
"""
import matplotlib.pyplot as plt

# Days of the month (1 to 31)
days = list(range(1, 32))

# Daily temperature data in Fahrenheit (replace with your own data)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line plot
plt.plot(days, temperature, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)

# Add x-axis label
plt.xlabel('Day of the Month')

# Add y-axis label
plt.ylabel('Temperature (°F)')

# Add a title to the chart
plt.title('Daily Temperature Changes Over the Month')

# Add grid lines for better readability
plt.grid(True)

# Display the plot
plt.show()

"""
Conclusion:
From the line plot, you can observe:

Temperature Trend: Identify whether there are any clear trends, such as increasing or decreasing temperatures over the days.
Peak and Low Temperatures: Determine the highest and lowest temperatures recorded and when they occurred.
Consistency: See if there are periods of consistent temperatures or significant fluctuations.
"""
