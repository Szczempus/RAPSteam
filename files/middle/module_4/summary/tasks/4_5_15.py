from collections import Counter


def char_frequency(text):
    """Zwraca słownik z częstością występowania znaków w podanym tekście (ignoruje wielkość liter)."""
    text = text.lower()  # Ignorowanie wielkości liter
    return dict(Counter(text))


print(char_frequency("Hello World"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
