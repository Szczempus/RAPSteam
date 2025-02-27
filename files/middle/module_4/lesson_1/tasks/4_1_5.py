def dane_osobowe(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")


# Przykładowe wywołanie
print(dane_osobowe(imie="Jan", nazwisko="Kowalski", wiek=25))
