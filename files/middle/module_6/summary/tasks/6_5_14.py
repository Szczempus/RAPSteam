import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dane cen mieszkań dla różnych miast
ceny_miasta = {
    "Warszawa": [6000, 7000, 8000, 9000, 10000],
    "Kraków": [5000, 6000, 6500, 7000, 7500],
    "Wrocław": [4000, 5000, 5500, 6000, 6500]
}


def rysuj_wykres():
    miasto = wybor.get()
    ceny = ceny_miasta.get(miasto, [])

    ax.clear()
    ax.plot(ceny, marker='o', linestyle='-')
    ax.set_title(f"Ceny mieszkań w {miasto}")
    ax.set_xlabel("Rok")
    ax.set_ylabel("Cena za m (PLN)")
    canvas.draw()


# Tworzenie okna aplikacji
root = tk.Tk()
root.title("Ceny mieszkań")

# Menu wyboru miasta
wybor = ttk.Combobox(root, values=list(ceny_miasta.keys()))
wybor.current(0)
wybor.pack()

# Przycisk rysowania wykresu
btn = tk.Button(root, text="Pokaż wykres", command=rysuj_wykres)
btn.pack()

# Wykres Matplotlib w Tkinter
fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
