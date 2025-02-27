def suma_wielu(*args):
    """Funkcja sumująca dowolną liczbę argumentów"""
    return sum(args)


print(suma_wielu(1, 2, 3, 4, 5))  # Wynik: 15


def informacje(**kwargs):
    """Funkcja wypisująca podane argumenty w postaci słownika"""
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")


informacje(imie="Kasia", wiek=30, miasto="Warszawa")
