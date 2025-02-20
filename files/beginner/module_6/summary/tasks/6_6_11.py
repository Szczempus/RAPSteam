from datetime import datetime

year = datetime.now().year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

with open("rok_info.txt", "w", encoding="utf-8") as file:
    file.write(f"Rok {year} {'jest' if is_leap else 'nie jest'} przestępny.\n")

print(f"Sprawdzenie zapisano do rok_info.txt")
