#Input: 16

def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

n = int(input("Podaj liczbę: "))
print_multiplication_table(n)

