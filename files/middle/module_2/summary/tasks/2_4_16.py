# Input: Jan 25 Niebieski

name, age, color = input("Podaj imię, wiek i ulubiony kolor: ").split()
user_tuple = (name, int(age), color)
print(f"Krotka: {user_tuple}")
