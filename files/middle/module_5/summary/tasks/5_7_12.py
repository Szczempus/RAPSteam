# Input: Zdanie 1., Zdanie 2., Zdanie 3.

# Tworzenie pliku
open("lista.txt", "w", encoding="utf-8").close()

# Pobranie zdań od użytkownika
zdania = [input(f"Podaj zdanie {i + 1}: ") for i in range(2)]

with open("lista.txt", "w", encoding="utf-8") as plik:
    for i, zdanie in enumerate(zdania, start=1):
        plik.write(f"{i}. {zdanie}\n")

print("Zapisano zdania do pliku 'lista.txt'.")
