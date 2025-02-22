try:
    with open("dane.txt", "r") as plik:
        zawartosc = plik.read()
        print("Zawartość pliku:")
        print(zawartosc)
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")
