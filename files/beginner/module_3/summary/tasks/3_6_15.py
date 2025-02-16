# Input: 15

temp = float(input("Podaj temperaturę: "))
if temp < 10:
    print("Niska")
elif temp <= 25:
    print("Umiarkowana")
else:
    print("Wysoka")
