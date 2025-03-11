# Plik: advanced_if.py
# Input: 3,5

# Pobranie dwóch liczb od użytkownika
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Obliczenie średniej
srednia = (a + b) / 2

# Sprawdzenie warunków i wypisanie wyniku
if srednia > 5:
    print("Bardzo dobrze")
elif srednia > 3:
    print("Zdane")
else:
    print("Nie zdane")
