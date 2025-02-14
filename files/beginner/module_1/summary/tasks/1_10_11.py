# Input: 1 2 3 6 5 4 7

wprowadzenie = input("Podaj 7 liczb oddzielonych spacjami: ").strip()
liczby_str = wprowadzenie.split()

liczby = []

for liczba in liczby_str:
    liczby.append(int(liczba))

zbior = set(liczby)

posortowane = list(zbior)

mediana = posortowane[3]
print(f"Mediana: {mediana:.2f}")
