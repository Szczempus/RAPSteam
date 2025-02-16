# Input: 15

wiek = int(input("Podaj swój wiek: "))

if wiek >= 18:
    print("Możesz prowadzić: rower, motorower, samochód.")
elif wiek >= 14:
    print("Możesz prowadzić: rower, motorower.")
elif wiek >= 10:
    print("Możesz prowadzić: rower.")
else:
    print("Nie masz jeszcze uprawnień do prowadzenia pojazdów.")
