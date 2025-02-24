import matplotlib
import matplotlib.pyplot as plt

# Dane: lata i ceny mieszkań
lata = [2010, 2012, 2014, 2016, 2018, 2020, 2022]
ceny = [3000, 3500, 4000, 4500, 5000, 6000, 7000]

matplotlib.use("TkAgg")

# Tworzenie wykresu liniowego
plt.figure(figsize=(8, 5))
plt.plot(lata, ceny, marker='o', linestyle='-', color='b')
plt.xlabel('Rok')
plt.ylabel('Cena za m (PLN)')
plt.title('Zmiana cen mieszkań w czasie')
plt.grid()
plt.show()
