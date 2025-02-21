import matplotlib.pyplot as plt
import pandas as pd

# Przykładowe dane zmian cen mieszkań w czasie
dane = {"Rok": [2018, 2019, 2020, 2021, 2022], "Cena za m² (PLN)": [7000, 7500, 8200, 8800, 9400]}
df = pd.DataFrame(dane)

# Tworzenie wykresu liniowego
plt.plot(df["Rok"], df["Cena za m² (PLN)"], marker="o", linestyle="-", color="red")

# Opisy osi i tytuł
plt.xlabel("Rok")
plt.ylabel("Cena za m² (PLN)")
plt.title("Zmiany średnich cen mieszkań w Warszawie")

# Wyświetlenie wykresu
plt.show()
