import pandas as pd

# Wczytanie danych
df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Wrocław', 'Gdańsk'],
    'Cena za m': [10000, 8000, 7000, 11000]
})

# Filtracja - miasta z ceną powyżej 10 000 PLN/m²
filtrowane = df[df['Cena za m'] > 10000]

print(filtrowane)
