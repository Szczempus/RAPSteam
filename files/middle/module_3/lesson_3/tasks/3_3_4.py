
# Define the input list
input_list = ['a', 'b', 'c']

# Use list comprehension with enumerate to create the list of tuples
result = [(index, value) for index, value in enumerate(input_list)]

# Print the result
print(result)
