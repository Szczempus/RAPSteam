import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Przycisk Tkinter")


# Funkcja po kliknięciu
def pokaz_komunikat():
    messagebox.showinfo("Wiadomość", "Witaj!")


button = tk.Button(root, text="Kliknij mnie!", command=pokaz_komunikat)
button.pack(pady=20)

root.mainloop()
