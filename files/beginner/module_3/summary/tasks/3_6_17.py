# Input: 70 1.75

waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

bmi = waga / (wzrost ** 2)

if bmi < 18.5:
    kategoria = "niedowaga"
elif 18.5 <= bmi < 25:
    kategoria = "norma"
elif 25 <= bmi < 30:
    kategoria = "nadwaga"
else:
    kategoria = "otyłość"

print(f"Twoje BMI wynosi: {bmi:.2f}. Kategoria: {kategoria}.")
