# Input: 12-345

postal_code = input("Podaj kod pocztowy (XX-XXX): ")
if len(postal_code) == 6 and postal_code[2] == "-" and postal_code.replace("-", "").isdigit():
    print("Poprawny kod pocztowy")
else:
    print("Błędny kod pocztowy")
