import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Ndz"]
wartosci = [10, 15, 7, 20, 25, 30, 5]

plt.bar(dni, wartosci)
plt.show()
