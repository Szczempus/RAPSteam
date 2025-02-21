import tkinter as tk
from tkinter import messagebox

# Tworzenie głównego okna Tkinter
root = tk.Tk()
root.withdraw()  # Ukrywa główne okno

# Wyświetlenie wersji Tkinter w komunikacie
messagebox.showinfo("Wersja Tkinter", f"Zainstalowana wersja Tkinter: {tk.TkVersion}")

# Zamykanie aplikacji po wyświetleniu komunikatu
root.destroy()
