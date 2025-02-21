#Input: 14543

def recursive_digit_sum(n):
    """
    Rekurencyjnie sumuje cyfry liczby, aż wynik będzie jednocyfrowy.

    Args:
    n (int): Liczba, której cyfry mają być sumowane.

    Returns:
    int: Jednocyfrowa suma cyfr liczby.
    """
    # Warunek zakończenia: jeśli n jest jednocyfrowe, zwróć n
    if n < 10:
        return n
    else:
        digit_sum = sum(int(digit) for digit in str(n))
        return recursive_digit_sum(digit_sum)
    
number = int(input("Podaj liczbę: "))
print(recursive_digit_sum(number))