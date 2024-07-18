#Write a Python program to get the largest and smallest number from a list without builtin functions.

def find_largest_and_smallest(numbers):
    # Initialize the first element as both the largest and smallest
    if len(numbers) == 0:
        return None, None  # Handle empty list case

    largest = numbers[0]
    smallest = numbers[0]
    
    # Iterate through the list starting from the second element
    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    
    return largest, smallest

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

largest, smallest = find_largest_and_smallest(numbers)

print("The largest number is:", largest)
print("The smallest number is:", smallest)


"""
output:
The largest number is: 9
The smallest number is: 1
"""
