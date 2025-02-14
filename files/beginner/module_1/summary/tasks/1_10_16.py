# Input: 175 80

wzrost_cm = float(input("Podaj wzrost w centymetrach: "))
waga_kg = float(input("Podaj wagę w kilogramach: "))

wzrost_m = wzrost_cm / 100

bmi = waga_kg / (wzrost_m ** 2)

print(f"\nTwoje BMI wynosi: {bmi:.2f}")
