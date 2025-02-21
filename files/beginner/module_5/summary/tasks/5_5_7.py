#Input: 1221

def is_prime(n):
    """
    Sprawdza, czy liczba n jest pierwsza.

    Parametry:
    n (int): Liczba do sprawdzenia.

    Zwraca:
    bool: True, jeśli liczba jest pierwsza, False w przeciwnym razie.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Podaj liczbę: "))
print(f"Liczba {number} jest liczbą pierwszą: {is_prime(number)}")

