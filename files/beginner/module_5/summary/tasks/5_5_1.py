#Input: 5

def count_down(n):
    """
    Wypisuje liczby od n do 1 przy użyciu pętli while.

    Parametry:
    n (int): liczba początkowa od której zaczyna się odliczanie
    """
    while n > 0:
        print(n)
        n -= 1

number = int(input("Podaj liczbę: "))
count_down(number)