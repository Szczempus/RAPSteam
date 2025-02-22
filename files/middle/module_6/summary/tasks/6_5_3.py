import tkinter as tk


def pokaz_dane():
    dane = f"Imię: {entry_imie.get()}, Nazwisko: {entry_nazwisko.get()}, Wiek: {entry_wiek.get()}"
    label_wynik.config(text=dane)


root = tk.Tk()
root.title("Formularz")

entry_imie = tk.Entry(root)
entry_imie.pack()
entry_nazwisko = tk.Entry(root)
entry_nazwisko.pack()
entry_wiek = tk.Entry(root)
entry_wiek.pack()

button = tk.Button(root, text="Wyświetl dane", command=pokaz_dane)
button.pack()
label_wynik = tk.Label(root, text="")
label_wynik.pack()

root.mainloop()
