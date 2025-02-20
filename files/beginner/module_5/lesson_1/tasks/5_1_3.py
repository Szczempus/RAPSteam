
def is_even(number):
    """
    Sprawdza, czy podana liczba całkowita jest parzysta.

    Parametry:
    number (int): Liczba całkowita do sprawdzenia.

    Zwraca:
    bool: True, jeśli liczba jest parzysta, False w przeciwnym przypadku.
    """
    return number % 2 == 0

print(f"Liczba 55 jest parzysta? {is_even(55)}")