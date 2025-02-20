
def policz_slowa(zdanie):
    """
    Ta funkcja przyjmuje zdanie jako ciąg znaków i zwraca liczbę słów w nim zawartych.
    Jeśli argument nie jest typu str, wypisuje komunikat o błędzie w konsoli.
    
    Parametry:
    Zdanie: str, zdanie, w którym liczymy słowa
    
    Zwraca:
    int, liczba słów w zdaniu
    """
    if not isinstance(zdanie, str):
        print("Nieprawidłowy typ argumentu. Oczekiwano ciągu znaków.")
        return None
    
    slowa = zdanie.split()
    return len(slowa)

print(f"Zdanie 'Ala ma kota' zawiera {policz_slowa('Ala ma kota')} słów.")
