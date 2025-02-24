# Input: 123-456-789

phone = input("Podaj numer telefonu w formacie xxx-xxx-xxx: ")
parts = phone.split("-")
if len(parts) == 3 and all(part.isdigit() and len(part) == 3 for part in parts):
    print("Poprawny numer telefonu")
else:
    print("Błędny numer telefonu")
