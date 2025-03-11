# Zadanie: 1_8_2.py

import turtle

star = turtle.Turtle()

# Tworzenie żółwia
t = turtle.Turtle()
t.speed(3)

# Rysowanie trójkąta bez pętli
t.forward(100)  # Pierwszy bok
t.left(120)

t.forward(100)  # Drugi bok
t.left(120)

t.forward(100)  # Trzeci bok
t.left(120)

# Zakończenie rysowania
turtle.done()