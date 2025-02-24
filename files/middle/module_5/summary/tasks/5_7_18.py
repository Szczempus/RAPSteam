import json

dane = {
    "osoby": [
        {"imie": "Anna", "nazwisko": "Kowalska", "wiek": 28},
        {"imie": "Piotr", "nazwisko": "Nowak", "wiek": 35},
        {"imie": "Kamil", "nazwisko": "Zieliński", "wiek": 22}
    ]
}

# Zapis do pliku JSON
with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump(dane, plik, indent=4, ensure_ascii=False)

print("Plik 'dane.json' został utworzony i zapisany.")
