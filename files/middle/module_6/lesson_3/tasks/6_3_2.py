import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv("ceny_mieszkan.csv")

# Wyświetlenie pierwszych 5 wierszy
print(df.head())
