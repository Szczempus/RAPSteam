# Input: 100,dolar

amount = float(input("Podaj kwotę w zł: "))
currency = input("Podaj walutę (dolar/euro): ")
exchange_rates = {"dolar": 3.97, "euro": 4.16}
if currency in exchange_rates:
    print(f"Kwota w {currency}: {amount / exchange_rates[currency]:.2f}")
else:
    print("Nieznana waluta")
