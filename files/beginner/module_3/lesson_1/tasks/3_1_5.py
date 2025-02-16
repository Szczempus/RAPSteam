# Input: Passw0rd

password = input("Podaj hasło: ")
has_min_length = len(password) >= 8
has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)

print(has_min_length and has_digit and has_upper)  # True
