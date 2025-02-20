# Tworzenie i zapis do pliku (tryb 'w' - nadpisanie)
with open("plik.txt", "w", encoding="utf-8") as file:
    file.write("Pierwsza linia\nDruga linia\nTrzecia linia\n")

# Dopisywanie do pliku (tryb 'a' - dodawanie)
with open("plik.txt", "a", encoding="utf-8") as file:
    file.write("Czwarta linia - dopisana\n")

# Odczyt pliku (tryb 'r' - tylko odczyt)
try:
    with open("plik.txt", "r", encoding="utf-8") as file:
        print("Zawartość pliku:")
        print(file.read())
except FileNotFoundError:
    print("Plik nie istnieje.")
