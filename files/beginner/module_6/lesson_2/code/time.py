import os
from datetime import datetime

# Pobranie aktualnej daty i czasu oraz formatowanie
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Aktualna data i czas:", formatted_date)

# Obliczanie różnicy między dwiema datami
date1 = datetime(2025, 2, 20)
date2 = datetime(2025, 3, 5)
print("Różnica dni:", (date2 - date1).days)

# Tworzenie pliku z datą w nazwie
log_filename = f"log_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
with open(log_filename, "w") as file:
    file.write(f"Log: {formatted_date}\n")

# Tworzenie katalogu z datą w nazwie
folder_name = now.strftime("backup_%Y-%m-%d")
os.makedirs(folder_name, exist_ok=True)

print(f"Utworzono plik: {log_filename}")  # Wyświetlenie nazwy pliku
print(f"Utworzono katalog: {folder_name}")  # Wyświetlenie nazwy katalogu
