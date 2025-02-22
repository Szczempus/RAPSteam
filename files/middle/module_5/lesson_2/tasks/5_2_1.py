# Input: 1 0

try:
    a, b = map(int, input("Podaj dwie liczby oddzielone spacją: ").split())
    wynik = a / b
    print(f"Wynik dzielenia: {wynik}")
except ZeroDivisionError:
    print("Błąd: Nie można dzielić przez zero!")
except ValueError:
    print("Błąd: Wprowadź poprawne liczby!")
