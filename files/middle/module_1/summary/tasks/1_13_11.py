# Input: 4, 5, 3, 2

first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))
third = int(input("Podaj trzecią liczbę: "))
fourth = int(input("Podaj czwartą liczbę: "))

suma_z_liczb = first + second + third + fourth

print(f"Typ zmiennej przed dzieleniem{type(suma_z_liczb)}")

suma_z_liczb = suma_z_liczb / 4

print(f"Typ zmiennej po dzieleniu{type(suma_z_liczb)}")

print(f"Średnia arytmetyczna z podanych liczb to: {suma_z_liczb}")

