# Input: 4, 8, 12

first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))
third = int(input("Podaj trzecią liczbę: "))

tablica_liczb = []

tablica_liczb.append(first)
tablica_liczb.append(second)    
tablica_liczb.append(third)

print(f"Średnia: {sum(tablica_liczb)/ len(tablica_liczb)}")
