# Input: 35

import math
import turtle

promien = float(input("Podaj promień okręgu: "))

t = turtle.Turtle()

t.circle(promien)

obwod = 2 * math.pi * promien
pole = math.pi * promien ** 2

print(f"Obwód okręgu: {obwod:.2f}")
print(f"Pole okręgu: {pole:.2f}")

turtle.done()
