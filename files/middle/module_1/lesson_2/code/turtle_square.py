# Plik: turtle_square.py

import turtle

# Tworzenie obiektu "żółwia"
zolw = turtle.Turtle()

# Rysowanie kwadratu
for x in range(4):
    zolw.forward(100)  # Przesuwa żółwia do przodu o 100 pikseli
    zolw.right(90)  # Obraca żółwia o 90 stopni w prawo

# Zamknięcie okna po kliknięciu
turtle.done()
