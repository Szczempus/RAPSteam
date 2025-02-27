# Input: Niemcy

kraje = {"Polska": "Warszawa", "Niemcy": "Berlin", "Francja": "Paryż"}

try:
    kraj = input("Podaj nazwę kraju: ")
    print(f"Stolica {kraj} to {kraje[kraj]}")
except KeyError:
    print("Błąd: Nie znaleziono tego kraju w słowniku.")
