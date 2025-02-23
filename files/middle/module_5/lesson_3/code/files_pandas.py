import pandas as pd

# Tworzenie DataFrame
dane = pd.DataFrame({
    "imie": ["Anna", "Jan"],
    "nazwisko": ["Kowalska", "Nowak"],
    "wiek": [25, 30]
})

# Zapis do pliku CSV z separatorem przecinka (domyślnie)
dane.to_csv("dane_comma.csv", index=False, encoding="utf-8")

# Zapis do pliku CSV z separatorem średnika
dane.to_csv("dane_semicolon.csv", sep=";", index=False, encoding="utf-8")

# Zapis do pliku CSV z separatorem tabulatora
dane.to_csv("dane_tab.csv", sep="\t", index=False, encoding="utf-8")

print("Pliki CSV zostały zapisane z różnymi separatorami.")
