
def custom_sequence(n):
    if n == 0:
        return 2
    else:
        return 3 * custom_sequence(n - 1) + 1

# Example usage:
print(custom_sequence(5))  # This will print the 5th term of the sequence
