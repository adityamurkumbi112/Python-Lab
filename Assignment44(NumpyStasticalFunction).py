"""
Compute the standard deviation of the NumPy array

 Input: arr = [20, 2, 7, 1, 34]
"""

import numpy as np

# Input array
arr = np.array([20, 2, 7, 1, 34])

# Compute the standard deviation of the array with default precision
std_dev = np.std(arr)

# Convert the array to float32 and compute the standard deviation
arr_float32 = arr.astype(np.float32)
std_dev_float32 = np.std(arr_float32)

# Convert the array to float64 and compute the standard deviation
arr_float64 = arr.astype(np.float64)
std_dev_float64 = np.std(arr_float64)

# Print the results
# The initial array and its standard deviation with default precision
print(f"arr :  {arr.tolist()}")
print(f"std of arr :  {std_dev}")

# The standard deviation computed using float32 precision
print("\nMore precision with float32")
print(f"std of arr :  {std_dev_float32}")

# The standard deviation computed using float64 precision
print("\nMore accuracy with float64")
print(f"std of arr :  {std_dev_float64}")


"""
Output:
arr :  [20, 2, 7, 1, 34]
std of arr :  12.576167937809991

More precision with float32
std of arr :  12.576168060302734

More accuracy with float64
std of arr :  12.576167937809991
"""
