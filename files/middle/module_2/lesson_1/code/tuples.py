# Tworzenie krotki
kolory = ("czerwony", "zielony", "niebieski")

# Dostęp do elementów
print(kolory[0])  # "czerwony"

# Próba modyfikacji spowoduje błąd
# kolory[1] = "żółty"  # TypeError: 'tuple' object does not support item assignment

# Krotki są przydatne np. do przechowywania stałych wartości, np. współrzędnych
punkt = (10, 20)
print(f"Pozycja punktu: x={punkt[0]}, y={punkt[1]}")
