import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Przykładowe ceny mieszkań
ceny = np.random.normal(5000, 1000, 200)  # Symulowane ceny mieszkań

matplotlib.use("TkAgg")

# Tworzenie histogramu
plt.figure(figsize=(8, 5))
plt.hist(ceny, bins=15, edgecolor='black', alpha=0.7)
plt.xlabel('Cena za m (PLN)')
plt.ylabel('Liczba mieszkań')
plt.title('Rozkład cen mieszkań')
plt.show()
