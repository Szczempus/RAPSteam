
def divisible_by_three(lst):
    return [x for x in lst if x % 3 == 0]

numbers = [1, 3, 4, 6, 9, 11, 12]
print(f"Lista liczb: {numbers}")
print(divisible_by_three(numbers))  

