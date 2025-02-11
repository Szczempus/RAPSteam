# Plik: turtle_square.py

import turtle

# Utworzenie "żółwia"
t = turtle.Turtle()  

# 4-krotne przejście o 100 jednostek do przodu
# i o brót o 90 stopni w lewo
for _ in range(4):
    t.forward(100)
    t.left(90)      

# Zakończenie ruchów żółwia
turtle.done()       