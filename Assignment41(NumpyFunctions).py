"""Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])"""

import numpy as np

# Given temperature data (extended to include cold days for demonstration purposes)
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, -4.0, -12.0])

# Identifying hot days where temperature > 35 degrees Celsius
hot_days = np.where(temperatures > 35)[0]

# Identifying cold days where temperature < 5 degrees Celsius
cold_days = np.where(temperatures < 5)[0]

# Printing the results in the desired format
print("Hot Days:")
print("Day\tTemperature (°C)")
# Iterating over the indices of hot days and printing the day and temperature
for day in hot_days:
    # Adding 1 to the index to match the day number (assuming the first day is day 1)
    print(f"{day+1}\t{temperatures[day]}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
# Iterating over the indices of cold days and printing the day and temperature
for day in cold_days:
    # Adding 1 to the index to match the day number (assuming the first day is day 1)
    print(f"{day+1}\t{temperatures[day]}")



"""
output:
Hot Days:
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature (°C)
11	4.0
12	-4.0
13	-12.0
"""
