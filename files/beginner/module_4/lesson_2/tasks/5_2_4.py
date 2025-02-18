# Input: 2.5, 3.5

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print(f"Suma: {a + b}")
print(f"Różnica: {a - b}")
print(f"Iloczyn: {a * b}")
print(f"Iloraz: {a / b if b != 0 else 'Nie można dzielić przez zero'}")
