# Tworzenie przykładowego pliku
tekst_przykladowy = """Pierwsza linia.

Druga linia.

Trzecia linia."""

with open("tekst.txt", "w", encoding="utf-8") as plik:
    plik.write(tekst_przykladowy)

# Usuwanie pustych linii
with open("tekst.txt", "r", encoding="utf-8") as plik:
    linie = [linia for linia in plik if linia.strip()]

with open("tekst.txt", "w", encoding="utf-8") as plik:
    plik.writelines(linie)

print("Plik 'tekst.txt' został zapisany bez pustych linii.")
