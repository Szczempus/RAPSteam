def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.read()
            print("Zawartość pliku:")
            print(zawartosc)
    except FileNotFoundError:
        print("Błąd: Plik nie został znaleziony.")
    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu pliku.")
    except IsADirectoryError:
        print("Błąd: Oczekiwano pliku, ale podano katalog.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


# Przykładowe wywołanie funkcji
wczytaj_plik("dane.txt")
