# Plik: today_date.py

# Przykład funkcji z długą nazwą
from datetime import datetime

# Pobranie aktualnej daty i godziny
dzisiaj = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Zapis do pliku
with open("data_log.txt", "a") as plik:
    plik.write(f"{dzisiaj}\n")

print(f"Dzisiejsza data została zapisana: {dzisiaj}")
