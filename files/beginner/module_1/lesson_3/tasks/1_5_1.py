# Argumenty: 4 2

# Pobranie dwóch liczb od użytkownika
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

# Obliczenia
suma = a + b
roznica = a - b
iloczyn = a * b
dzielenie_calkowite = a // b if b != 0 else "Nie można dzielić przez zero!"

# Wyświetlenie wyników
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")
print(f"Dzielenie całkowite: {dzielenie_calkowite}")
