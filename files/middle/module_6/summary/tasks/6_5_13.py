import matplotlib.pyplot as plt
import numpy as np

# Przykładowe ceny mieszkań
ceny = np.random.normal(5000, 1000, 200)  # Symulowane ceny mieszkań

# Tworzenie histogramu
plt.figure(figsize=(8, 5))
plt.hist(ceny, bins=15, edgecolor='black', alpha=0.7)
plt.xlabel('Cena za m² (PLN)')
plt.ylabel('Liczba mieszkań')
plt.title('Rozkład cen mieszkań')
plt.show()
