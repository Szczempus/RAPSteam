from statistics import mean

# Pobranie trzech liczb od użytkownika w jednej linii
numbers = list(map(float, input("Podaj trzy liczby: ").split()))

# Obliczenie średniej arytmetycznej za pomocą mean()
srednia = mean(numbers)

# Wyświetlenie wyniku
print(f"Średnia: {srednia:.2f}")
