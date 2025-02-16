# Input: 123456

number = input("Podaj liczbę: ")
# Sprawdzenie, czy liczba zaczyna się od "-" i reszta to cyfry
if number.startswith("-") and number[1:].isdigit():
    print("Podana wartość jest liczbą całkowitą ujemną.")
else:
    print("Podana wartość nie jest liczbą całkowitą ujemną.")
