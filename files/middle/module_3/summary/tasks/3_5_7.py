
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(digit) for digit in str(n)))

# Przykład użycia
print(digital_root(942))  # Output: 6
print(digital_root(16))   # Output: 7
print(digital_root(132189))  # Output: 6