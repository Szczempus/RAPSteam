# Input: 5

import math

# Pobranie liczby od użytkownika
liczba = float(input("Podaj liczbę: "))

# Obliczenie pierwiastka kwadratowego
if liczba >= 0:
    wynik = math.sqrt(liczba)
    print(f"Pierwiastek kwadratowy z {liczba} wynosi {wynik}")
else:
    print("Nie można obliczyć pierwiastka kwadratowego z liczby ujemnej.")
