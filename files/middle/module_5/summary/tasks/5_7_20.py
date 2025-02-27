import pandas as pd

# Wczytanie pliku CSV do Pandas
df = pd.read_csv("dane.csv")

# Dodanie nowej kolumny
df["Rok_urodzenia"] = 2024 - df["Wiek"]

# Zapis zaktualizowanych danych do nowego pliku
df.to_csv("dane_z_rokiem.csv", index=False)

print("Nowy plik 'dane_z_rokiem.csv' został zapisany.")
print(df)
