# Input: 4,2

# Pobranie dwóch liczb od użytkownika
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Wyświetlenie wyników
print(f"Suma: {a + b}")
print(f"Różnica: {a - b}")
print(f"Iloczyn: {a * b}")
print(f"Dzielenie całkowite: {a // b if b != 0 else 'Nie można dzielić przez zero!'}")
