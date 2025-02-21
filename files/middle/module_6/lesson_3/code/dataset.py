import pandas as pd

# Tworzenie przykładowych danych - średnie ceny mieszkań w miastach
dane = {
    "Miasto": ["Warszawa", "Kraków", "Wrocław", "Poznań", "Gdańsk", "Łódź"],
    "Cena za m² (PLN)": [12500, 10500, 9500, 8700, 11200, 7500]
}

# Tworzenie DataFrame
df = pd.DataFrame(dane)

# Zapis do pliku CSV
df.to_csv("ceny_mieszkan.csv", index=False)

print("Plik 'ceny_mieszkan.csv' został zapisany.")
