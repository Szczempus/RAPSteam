import os

filename = "dane.txt"

if os.path.exists(filename):
    can_read = os.access(filename, os.R_OK)
    can_write = os.access(filename, os.W_OK)
    print(f"Plik {filename} - Odczyt: {'Tak' if can_read else 'Nie'}, Zapis: {'Tak' if can_write else 'Nie'}")
else:
    print(f"Plik {filename} nie istnieje.")
