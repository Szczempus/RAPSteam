# Input: 1

liczba = input("Podaj liczbę: ")

if liczba.lstrip('-').isdigit():  # Sprawdzenie, czy liczba jest całkowita (obsługa ujemnych)
    liczba = int(liczba)
    if liczba > 0:
        print("Liczba jest dodatnia")
    elif liczba < 0:
        print("Liczba jest ujemna")
    else:
        print("Liczba to zero")
else:
    print("To nie jest poprawna liczba całkowita")
