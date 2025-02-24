kraje = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryż",
    "Włochy": "Rzym"
}

try:
    kraj = input("Podaj nazwę kraju: ").strip()
    print(f"Stolica {kraj} to {kraje[kraj]}.")
except KeyError:
    print("Błąd: Nie znamy stolicy tego kraju!")
