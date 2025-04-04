import pandas as pd

# Wczytanie danych z CSV (zakładamy, że plik zawiera kolumnę 'Cena za m')
df = pd.read_csv('ceny_mieszkan.csv')

# Obliczenie średniej ceny
srednia_cena = df['Cena za m (PLN)'].mean()
print(f"Średnia cena mieszkań: {srednia_cena:.2f} PLN/m²")
