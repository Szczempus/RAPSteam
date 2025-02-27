import csv

dane = [
    ["Imię", "Nazwisko", "Wiek"],
    ["Anna", "Kowalska", 28],
    ["Piotr", "Nowak", 35],
    ["Kamil", "Zieliński", 22]
]

# Tworzenie i zapis do pliku CSV
with open("dane.csv", "w", newline="", encoding="utf-8") as plik:
    writer = csv.writer(plik)
    writer.writerows(dane)

print("Plik 'dane.csv' został utworzony i zapisany.")
