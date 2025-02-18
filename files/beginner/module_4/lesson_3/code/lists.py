# Tworzenie listy
owoce = ["jabłko", "banan", "wiśnia"]

# Dodawanie elementów
owoce.append("gruszka")  # ["jabłko", "banan", "wiśnia", "gruszka"]

# Usuwanie elementów
owoce.remove("banan")  # ["jabłko", "wiśnia", "gruszka"]
ostatni = owoce.pop()  # Usuwa ostatni element i zwraca go ("gruszka")

# Sortowanie listy
owoce.sort()  # ["jabłko", "wiśnia"]

print(owoce)
