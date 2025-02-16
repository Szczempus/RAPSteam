# Input: 25

wiek = int(input("Podaj liczbę: "))
if wiek < 13:
    print("Dziecko")
elif wiek < 18:
    print("Nastolatek")
else:
    print("Dorosły")
