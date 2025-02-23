class LiczbaUjemnaError(Exception):
    """Wyjątek zgłaszany, gdy liczba jest ujemna."""

    def __init__(self, liczba):
        super().__init__(f"Błąd: Podano liczbę ujemną ({liczba}). Oczekiwano liczby dodatniej.")
        self.liczba = liczba


def sprawdz_liczbe(liczba):
    if liczba < 0:
        raise LiczbaUjemnaError(liczba)
    return f"Podana liczba {liczba} jest poprawna."


try:
    x = int(input("Podaj liczbę dodatnią: "))
    print(sprawdz_liczbe(x))
except LiczbaUjemnaError as e:
    print(e)
