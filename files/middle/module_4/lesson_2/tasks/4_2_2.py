import random

# Wylosowanie 5 liczb z zakresu 1-100
losowe_liczby = random.sample(range(1, 101), 5)

# Posortowanie liczb
losowe_liczby.sort()

# Wyświetlenie wyników
print("Wylosowane liczby w kolejności rosnącej:", losowe_liczby)
