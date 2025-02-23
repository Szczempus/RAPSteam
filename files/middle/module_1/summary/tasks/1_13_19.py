# Input: 5

waga_kg = float(input("Podaj wagę w kilogramach: "))

waga_g = waga_kg * 1000
waga_funt = waga_kg * 2.20462

print(f"Waga w gramach: {waga_g:.2f} g")
print(f"Waga w funtach: {waga_funt:.2f} lb")
