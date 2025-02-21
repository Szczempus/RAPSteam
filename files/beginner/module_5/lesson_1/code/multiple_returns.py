
def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count != 0 else 0
    return total, count, average

numbers = [1, 2, 3, 4, 5]
total, count, average = calculate_statistics(numbers)
print(f"Total: {total}, Count: {count}, Average: {average}")