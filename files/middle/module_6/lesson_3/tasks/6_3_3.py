import matplotlib.pyplot as plt
import pandas as pd

# Wczytanie danych
df = pd.read_csv("ceny_mieszkan.csv")

# Tworzenie wykresu słupkowego
plt.figure(figsize=(8, 5))
plt.bar(df["Miasto"], df["Cena za m² (PLN)"], color="blue")

# Opisy osi i tytuł
plt.xlabel("Miasto")
plt.ylabel("Cena za m² (PLN)")
plt.title("Średnie ceny mieszkań w różnych miastach")

# Wyświetlenie wykresu
plt.show()
