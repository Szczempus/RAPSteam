
# Lista liczb
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Nowa lista do przechowywania wyników
result = []

# Indeks początkowy
index = 0

# Pętla while do iteracji przez listę liczb
while index < len(numbers):
    if numbers[index] > 50:
        break
    result.append(numbers[index])
    index += 1

# Wypisanie utworzonej listy
print(result)
