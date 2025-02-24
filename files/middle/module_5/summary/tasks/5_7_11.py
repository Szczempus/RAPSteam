# Tworzenie pliku, jeśli nie istnieje
tekst_przykladowy = """To jest pierwsza linia.
To jest druga linia.
To jest trzecia linia."""

with open("tekst.txt", "w", encoding="utf-8") as plik:
    plik.write(tekst_przykladowy)

# Odczyt od końca
with open("tekst.txt", "r", encoding="utf-8") as plik:
    linie = plik.readlines()
    for linia in reversed(linie):
        print(linia.strip())
