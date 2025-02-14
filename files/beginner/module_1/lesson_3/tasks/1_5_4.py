# Input: 1 2 3 4 5

# Pobranie liczb jako jednego ciągu znaków
liczby = input("Podaj liczby oddzielone spacją: ")

# Konwersja na listę liczb całkowitych
lista_liczb = list(map(int, liczby.split()))

# Obliczenia
suma_liczb = sum(lista_liczb)
liczba_elementow = len(lista_liczb)

# Wyświetlenie wyników
print(f"Suma: {suma_liczb}\nLiczba elementów: {liczba_elementow}")
