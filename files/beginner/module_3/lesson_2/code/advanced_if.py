# Plik: advanced_if.py
# Input: 3,5

# Pobranie dwóch liczb od użytkownika
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Obliczenie średniej
srednia = (a + b) / 2

# Sprawdzenie warunku i wypisanie wyniku
if srednia > 3:
    print("Zdane")
else:
    print("Nie zdane")
