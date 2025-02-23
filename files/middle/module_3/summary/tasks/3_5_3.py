
def recursive_even_sum(lst):
    if not lst:
        return 0
    else:
        current = lst[0]
        rest_sum = recursive_even_sum(lst[1:])
        if current % 2 == 0:
            return current + rest_sum
        else:
            return rest_sum

# Przykład użycia:
print(recursive_even_sum([1, 2, 3, 4, 5, 6]))  # Output: 12
