
def square_list(numbers):
    return [number ** 2 for number in numbers]
 
numbers = [1, 2, 3, 4]
print(f"Numbers: {numbers}")
print(f"Squared numbers: {square_list(numbers)}")
