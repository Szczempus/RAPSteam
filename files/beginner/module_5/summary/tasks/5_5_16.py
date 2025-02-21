#Input: 5

def squares_list(n):  
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

n = int(input("Podaj liczbę: "))
print(squares_list(n))
