"""Write a Python script to concatenate the following dictionaries to create a new one. 

Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

 Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary and update it with the contents of dic1, dic2, and dic3
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Expected Result:", result)


"""
output:
Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
