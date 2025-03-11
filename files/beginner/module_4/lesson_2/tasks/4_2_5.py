# Input: 0.5

number = float(input("Enter a number: "))
integer_part = int(number)

binary_format = format(integer_part, 'b')
octal_format = format(integer_part, 'o')
hexadecimal_format = format(integer_part, 'x')

print(f"Binary: {binary_format}")
print(f"Octal: {octal_format}")
print(f"Hexadecimal: {hexadecimal_format}")
