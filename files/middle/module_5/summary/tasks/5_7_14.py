# Tworzenie pliku, jeśli nie istnieje
tekst_przykladowy = """To jest przykładowy plik.
Zawiera kilka linijek tekstu.
Można w nim wyszukiwać słowa."""

with open("tekst.txt", "w", encoding="utf-8") as plik:
    plik.write(tekst_przykladowy)

# Sprawdzenie, czy słowo istnieje w pliku
slowo = input("Podaj słowo do wyszukania w pliku: ")

with open("tekst.txt", "r", encoding="utf-8") as plik:
    zawartosc = plik.read()

if slowo in zawartosc:
    print(f"Słowo '{slowo}' znaleziono w pliku!")
else:
    print(f"Słowo '{slowo}' nie występuje w pliku.")
