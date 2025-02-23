#Input: 6

rows = int(input("Podaj liczbę wierszy: "))

for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()
