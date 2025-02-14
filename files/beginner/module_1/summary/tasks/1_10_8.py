a = float(input("Podaj długość pierwszego boku prostokąta (w cm): "))
b = float (input("Podaj długosć drugiego boku prostokąta (w cm): "))

obwod =  2 * (a + b)
pole = a * b 

print(f"\nObwód prostokąta: {obwod:.2f} cm")
print(f"Pole prostokąta: {pole:.2f} cm^2")