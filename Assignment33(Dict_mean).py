"""1. Write a Python program and calculate the mean of the below dictionary.

 test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

 Output: 6.2"""

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the sum of all values
total = sum(test_dict.values())

# Count the number of items
count = len(test_dict)

# Calculate the mean
mean = total / count

print(f"Output: {mean}")
