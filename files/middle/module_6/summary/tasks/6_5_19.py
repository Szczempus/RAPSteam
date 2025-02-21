import tkinter as tk


def dodaj_pole():
    nowe_pole = tk.Entry(root)
    nowe_pole.pack()
    pola.append(nowe_pole)


root = tk.Tk()
root.title("Dynamiczny formularz")

pola = []

btn_dodaj = tk.Button(root, text="Dodaj pole", command=dodaj_pole)
btn_dodaj.pack()

root.mainloop()
