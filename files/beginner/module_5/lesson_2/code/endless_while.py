# Input: 5,3,0

while True:
    user_input = input("Podaj liczbę (0, aby zakończyć): ")
    number = int(user_input)
    if number == 0:
        break
    print(f"Podałeś: {number}")
print("Koniec programu.")
