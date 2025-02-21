#Input: Kajak

def is_palindrome(s):
    """
    Sprawdza rekurencyjnie, czy łańcuch s jest palindromem.
    
    Argumenty:
    s -- łańcuch znaków do sprawdzenia
    
    Zwraca:
    True, jeśli łańcuch jest palindromem, w przeciwnym razie False
    """
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

word = input("Podaj słowo: ")
print(f"Słowo {word} {'jest' if is_palindrome(word) else 'nie jest'} palindromem")