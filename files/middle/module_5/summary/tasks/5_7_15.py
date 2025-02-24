import os
from datetime import datetime

# Tworzenie pliku, jeśli nie istnieje
if not os.path.exists("dziennik.txt"):
    open("dziennik.txt", "w", encoding="utf-8").close()

wpis = input("Podaj treść wpisu do dziennika: ")
data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("dziennik.txt", "a", encoding="utf-8") as plik:
    plik.write(f"[{data}] {wpis}\n")

print("Dodano wpis do dziennika!")
