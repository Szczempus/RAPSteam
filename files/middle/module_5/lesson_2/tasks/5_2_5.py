class PustyPlikError(Exception):
    """Wyjątek zgłaszany, gdy plik jest pusty."""

    def __init__(self, nazwa_pliku):
        super().__init__(f"Plik '{nazwa_pliku}' jest pusty.")


try:
    with open("dane.txt", "r") as plik:
        zawartosc = plik.read()
        if not zawartosc:
            raise PustyPlikError("dane.txt")
        print("Zawartość pliku:")
        print(zawartosc)
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")
except PustyPlikError as e:
    print(f"Błąd: {e}")
