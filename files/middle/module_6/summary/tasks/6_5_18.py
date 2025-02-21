import pandas as pd

# Przykładowe dane cen mieszkań w różnych miastach
df = pd.DataFrame({
    'Warszawa': [9000, 9500, 10000, 10500, 11000],
    'Kraków': [7000, 7500, 8000, 8500, 9000],
    'Wrocław': [6000, 6500, 7000, 7500, 8000]
})

# Obliczenie korelacji
korelacja = df.corr()

print(korelacja)
