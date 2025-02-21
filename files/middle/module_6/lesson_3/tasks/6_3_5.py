import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Wczytanie danych
df = pd.read_csv("ceny_mieszkan.csv")

# Normalizacja danych
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.iloc[:, 1:])

# Obliczenie korelacji
korelacja = cosine_similarity(scaled_data)

# Konwersja wyniku do DataFrame
df_korelacja = pd.DataFrame(korelacja, index=df["Miasto"], columns=df["Miasto"])

# Wyświetlenie macierzy korelacji
print(df_korelacja)
