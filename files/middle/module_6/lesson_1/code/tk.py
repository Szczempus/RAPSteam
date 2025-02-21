import tkinter as tk
from tkinter import messagebox

# Tworzenie głównego okna
root = tk.Tk()
root.title("Moja pierwsza aplikacja")


# Funkcja obsługująca kliknięcie przycisku
def pokaz_wiadomosc():
    messagebox.showinfo("Informacja", "Witaj w aplikacji!")


# Dodanie przycisku
przycisk = tk.Button(root, text="Kliknij mnie!", command=pokaz_wiadomosc)
przycisk.pack(pady=20)

# Uruchomienie aplikacji
root.mainloop()
