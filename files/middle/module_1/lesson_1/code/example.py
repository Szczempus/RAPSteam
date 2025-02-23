# Plik: example.py

# Importowanie modułu standardowego
import datetime


# Definicja funkcji
def greet(name):
    """Funkcja zwracająca powitanie dla podanej osoby."""
    return f"Cześć, {name}! Dzisiaj jest {datetime.date.today()}."  # Wcięcia 4 spacje


# Wywołanie funkcji, jeśli skrypt jest uruchamiany bezpośrednio
if __name__ == "__main__":
    print(greet("Patryk"))  # Wcięcia 4 spacje

print("Koniec skryptu")  # Wcięcia 0 spacji
