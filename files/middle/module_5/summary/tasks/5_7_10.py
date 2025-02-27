# Input: 150

class PrzekroczonoZakresError(Exception):
    pass


try:
    liczba = int(input("Podaj liczbę z zakresu 1-100: "))
    if liczba < 1 or liczba > 100:
        raise PrzekroczonoZakresError("Podana liczba wykracza poza dozwolony zakres!")
    print(f"Podana liczba ({liczba}) jest poprawna.")
except PrzekroczonoZakresError as e:
    print(f"Błąd: {e}")
except ValueError:
    print("Błąd: Podana wartość nie jest liczbą całkowitą!")
