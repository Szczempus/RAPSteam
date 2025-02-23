# Input: Jabłko 3 Banan 5 Pomarańcza 4

items = input("Podaj trzy produkty i ich ceny \n(np. Jabłko 3 Banan 5 Pomarańcza 4): ").split()
product_dict = {items[i]: int(items[i + 1]) for i in range(0, len(items), 2)}
for product, price in product_dict.items():
    print(f"{product}: {price} zł")
