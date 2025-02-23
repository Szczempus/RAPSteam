import csv

dane = [
    ['imie', 'nazwisko', 'wiek'],
    ['Anna', 'Kowalska', 25],
    ['Jan', 'Nowak', 30]
]

# Zapis do pliku CSV z separatorem przecinka
with open('dane_comma.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dane)

# Zapis do pliku CSV z separatorem średnika
with open('dane_semicolon.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(dane)

# Zapis do pliku CSV z separatorem tabulatora
with open('dane_tab.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(dane)
