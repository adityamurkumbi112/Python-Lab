"""Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

 Input: my_list = [1, 2, 3, 4, 5]"""

import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Display the NumPy array
print("Original array:", my_array)

# Display the first and last index
print("First element:", my_array[0])
print("Last element:", my_array[-1])

# Multiply each element by 2
multiplied_array = my_array * 2

# Display the result
print("Array after multiplying each element by 2:", multiplied_array)


"""
Output:
Original array: [1 2 3 4 5]
First element: 1
Last element: 5
Array after multiplying each element by 2: [ 2  4  6  8 10]
"""
