import pandas as pd

# Wczytanie danych
df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Wrocław', 'Gdańsk'],
    'Cena za m²': [10000, 8000, 7000, 7500]
})

# Sortowanie według ceny za m²
df_sorted = df.sort_values(by='Cena za m²')

print(df_sorted)
