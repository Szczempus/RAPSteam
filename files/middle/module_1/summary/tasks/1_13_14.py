# Input: 2024

year = int(input("Podaj rok: "))
print("Przestępny" if (year % 4 == 0 and year % 100 != 0)
                      or year % 400 == 0 else "Nieprzestępny")
