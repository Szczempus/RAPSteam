import os

filename = "dane.txt"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print("\nZawartość pliku:")
        print(file.read())
else:
    print(f"\nPlik '{filename}' nie istnieje.")
