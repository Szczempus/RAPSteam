import math

promien = float(input("Podaj promień podstawy walca (w cm): ")) 
wysokosc = float(input("Podaj wysokość walca (w cm): "))

pole_podstawy = math.pi * promien ** 2
objetosc = pole_podstawy * wysokosc

print(f"\nPole podstawy: {pole_podstawy:.2f} cm^2")
print(f"Objętość walca: {objetosc:.2f} cm^3")