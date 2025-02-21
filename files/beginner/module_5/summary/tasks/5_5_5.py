
def filter_even_numbers(lst):
    even_numbers = []
    for number in lst:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")