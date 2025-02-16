# Input: 150, 50

number = int(input("Podaj liczbę: "))
if not (1 <= number <= 100):
    number = int(input("Podaj poprawną liczbę (1-100): "))
print("Poprawna liczba:", number)
