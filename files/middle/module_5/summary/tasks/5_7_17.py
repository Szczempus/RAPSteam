import csv

wiek_sum = 0
liczba_osob = 0

# Odczyt pliku CSV
with open("dane.csv", "r", encoding="utf-8") as plik:
    reader = csv.reader(plik)
    next(reader)  # Pominięcie nagłówka
    for row in reader:
        wiek_sum += int(row[2])
        liczba_osob += 1

sredni_wiek = wiek_sum / liczba_osob
print(f"Średni wiek osób w pliku CSV wynosi: {sredni_wiek:.2f} lat")
