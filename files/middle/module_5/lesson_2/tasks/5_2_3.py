# Input: 6

liczby = [10, 20, 30, 40]

try:
    indeks = int(input("Podaj indeks elementu listy: "))
    print(f"Element na pozycji {indeks}: {liczby[indeks]}")
except IndexError:
    print("Błąd: Podano indeks spoza zakresu listy!")
except ValueError:
    print("Błąd: Wprowadź liczbę całkowitą!")
