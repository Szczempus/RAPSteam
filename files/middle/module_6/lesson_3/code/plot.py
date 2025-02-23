import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("TkAgg")  # Lub inny backend, np. Agg, Qt5Agg
# Wczytanie danych z pliku CSV
df = pd.read_csv("ceny_mieszkan.csv")

# Wyświetlenie tabeli
print(df)

# Tworzenie wykresu słupkowego
plt.figure(figsize=(8, 5))
plt.bar(df["Miasto"], df["Cena za m² (PLN)"], color=["blue", "green", "red", "orange", "purple", "gray"])

# Opisy osi i tytuł
plt.xlabel("Miasto")
plt.ylabel("Cena za m² (PLN)")
plt.title("Średnie ceny mieszkań w polskich miastach")

# Wyświetlenie wykresu
plt.show()
