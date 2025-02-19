# Input: 10 20 30 40 50

numbers = list(map(int, input("Podaj pięć liczb: ").split()))
numbers.pop(0)
print(f"Lista po usunięciu pierwszego elementu: {numbers}")
