
def triangular_number(n):
    if n == 1:
        return 1
    else:
        return n + triangular_number(n - 1)

# Przykład użycia
print(triangular_number(5))  # Output: 15

