from datetime import datetime

filename = "log.txt"
current_time = datetime.now()

with open(filename, "a", encoding="utf-8") as file:
    file.write(f"{current_time} - Nowe logowanie do systemu\n")

print(f"\nNowa linia została dopisana do '{filename}'.")
