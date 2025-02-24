# Input: 8 3 7 1 5

numbers = list(map(int, input("Podaj pięć liczb: ").split()))
numbers.sort()
print(f"Posortowana lista: {numbers}")
