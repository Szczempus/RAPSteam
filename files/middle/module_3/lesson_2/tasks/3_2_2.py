
def recursive_sum(numbers):
    def helper(numbers, current_sum):
        if not numbers:
            return current_sum
        return helper(numbers[1:], current_sum + numbers[0])
    
    return helper(numbers, 0)

numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 15

