# Input: 10 3

num1, num2 = map(int, input("Podaj dwie liczby: ").split())
result = num1 // num2
print(f"Dzielenie całkowite: {result}, typ wyniku: {type(result)}")
