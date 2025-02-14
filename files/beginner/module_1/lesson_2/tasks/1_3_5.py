from datetime import datetime

# Pobranie aktualnej daty i godziny w formacie YYYY-MM-DD HH:MM:SS
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Treść wpisu do loga
log_entry = f"{current_time} - Uruchomiono skrypt\n"

# Nazwa pliku loga
log_file = "log.txt"

# Otwarcie pliku w trybie dopisywania (lub utworzenie, jeśli nie istnieje)
with open(log_file, "a", encoding="utf-8") as file:
    file.write(log_entry)

print(f"Zapisano do {log_file}: {log_entry.strip()}")
