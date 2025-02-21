import tkinter as tk
from tkinter import ttk


def pokaz_wybor():
    label.config(text=f"Wybrane miasto: {combobox.get()}")


root = tk.Tk()
root.title("Combobox")

combobox = ttk.Combobox(root, values=["Warszawa", "Kraków", "Wrocław"])
combobox.pack()
button = tk.Button(root, text="Pokaż wybór", command=pokaz_wybor)
button.pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
