#Write a Python program to sum all the items in a list.

def sum_list(items):
    # Initialize a variable to keep the total sum
    total = 0
    
    # Iterate over each item in the list
    for item in items:
        # Add the current item to the total
        total += item
    
    # Return the total sum
    return total

# Example usage:
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Call the sum_list function with the list of numbers
result = sum_list(numbers)

# Print the result
print("The sum of the list is:", result)


#output:The sum of the list is: 15
