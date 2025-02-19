# Input: 4 8 12

numbers = list(map(float, input("Podaj trzy liczby: ").split()))
print(f"Średnia: {sum(numbers) / len(numbers)}")
