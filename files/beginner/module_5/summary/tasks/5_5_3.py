#Input: -40

def absolute_value(n):
    """
    Zwraca wartość bezwzględną liczby n.

    Parametry:
    n (int lub float): Liczba, dla której ma zostać obliczona wartość bezwzględna.

    Zwraca:
    int lub float: Wartość bezwzględna liczby n.
    """
    if n >= 0:
        return n
    else:
        return -n

number = int(input("Podaj liczbę: "))
print(absolute_value(number))
