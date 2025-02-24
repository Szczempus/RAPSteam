
def recursive_digit_product(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n
    else:
        # Recursive case: multiply the last digit by the product of the remaining digits
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit * recursive_digit_product(remaining_digits)

# Example usage:
print(recursive_digit_product(1234))  # Output: 24 (1*2*3*4)