from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")  # DD-MM-YYYY HH:MM:SS
print("Aktualna data i czas:", formatted_date)

backup_filename = f"backup_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
with open(backup_filename, "w", encoding="utf-8") as file:
    file.write(f"Backup wykonany o {formatted_date}\n")

print(f"\nUtworzono plik: {backup_filename}")
