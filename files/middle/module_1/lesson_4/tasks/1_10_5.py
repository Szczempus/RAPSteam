# Input: 1-2-3-4-5-6

wejscie = input("Podaj liczby oddzielone myślnikami (1-2-3-4-5-6): ")  # Pobranie danych
lista_liczb = list(map(int, wejscie.split("-")))  # Konwersja na listę liczb całkowitych

suma_liczb = sum(lista_liczb)  # Obliczenie sumy
srednia = suma_liczb / len(lista_liczb)  # Obliczenie średniej

print(f"Suma: {suma_liczb}, typ: {type(suma_liczb)}")
print(f"Średnia: {srednia}, typ: {type(srednia)}")
