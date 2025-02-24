import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def wczytaj_plik():
    plik = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if plik:
        global df
        df = pd.read_csv(plik)
        tekst.delete("1.0", tk.END)
        tekst.insert(tk.END, df.to_string())


def rysuj_wykres():
    if df is not None:
        ax.clear()
        df.groupby("Miasto")["Cena za m"].mean().plot(kind="bar", ax=ax)
        ax.set_title("Średnia cena mieszkań w miastach")
        canvas.draw()


root = tk.Tk()
root.title("Analiza cen mieszkań")

btn_wczytaj = tk.Button(root, text="Wczytaj plik CSV", command=wczytaj_plik)
btn_wczytaj.pack()

btn_wykres = tk.Button(root, text="Pokaż wykres", command=rysuj_wykres)
btn_wykres.pack()

tekst = tk.Text(root, height=10, width=50)
tekst.pack()

fig, ax = plt.subplots(figsize=(5, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
