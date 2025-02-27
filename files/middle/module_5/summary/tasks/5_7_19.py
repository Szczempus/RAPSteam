import json

# Odczyt pliku JSON
with open("dane.json", "r", encoding="utf-8") as plik:
    dane = json.load(plik)

# Znalezienie najstarszej osoby
najstarsza_osoba = max(dane["osoby"], key=lambda x: x["wiek"])
print(f"Najstarsza osoba: {najstarsza_osoba['imie']} {najstarsza_osoba['nazwisko']} ({najstarsza_osoba['wiek']} lat)")
