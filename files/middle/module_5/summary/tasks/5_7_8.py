#  Input: 1-2-3-4

try:
    wejscie = input("Podaj liczby oddzielone myślnikami: (1-2-3-4) ")
    liczby = [int(x.strip()) for x in wejscie.split(",")]
    print("Lista liczb:", liczby)
except ValueError:
    print("Błąd: Jedna z wartości nie jest liczbą! Pomiń błędne wartości i spróbuj ponownie.")
