import tkinter as tk
from tkinter import messagebox

# Tworzenie głównego okna
root = tk.Tk()
root.title("Formularz użytkownika")

# Etykieta i pole wejściowe dla imienia
tk.Label(root, text="Imię:").grid(row=0, column=0, padx=10, pady=5)
imie_entry = tk.Entry(root)
imie_entry.grid(row=0, column=1, padx=10, pady=5)

# Etykieta i pole wejściowe dla wieku
tk.Label(root, text="Wiek:").grid(row=1, column=0, padx=10, pady=5)
wiek_entry = tk.Entry(root)
wiek_entry.grid(row=1, column=1, padx=10, pady=5)


# Funkcja do pobrania i wyświetlenia danych
def wyswietl_dane():
    imie = imie_entry.get()
    wiek = wiek_entry.get()
    messagebox.showinfo("Dane użytkownika", f"Imię: {imie}\nWiek: {wiek}")


# Przycisk do przesyłania formularza
tk.Button(root, text="Wyślij", command=wyswietl_dane).grid(row=2, columnspan=2, pady=10)

# Uruchomienie aplikacji
root.mainloop()
