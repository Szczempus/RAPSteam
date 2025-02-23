import pandas as pd

# Tworzenie DataFrame
dane = pd.DataFrame({
    "imie": ["Anna", "Jan"],
    "nazwisko": ["Kowalska", "Nowak"],
    "wiek": [25, 30]
})

# Zapis do pliku JSON
dane.to_json("dane.json", orient="records", indent=4, force_ascii=False)

print("Plik JSON został zapisany.")

