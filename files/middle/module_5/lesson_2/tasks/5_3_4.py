filename = "dane.txt"
try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line.upper())

    print(f"\nZawartość pliku '{filename}' została zamieniona na wielkie litery.")
except FileNotFoundError:
    print(f"\nPlik '{filename}' nie istnieje.")
