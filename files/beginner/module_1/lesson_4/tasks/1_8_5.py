# Zadanie: 1_8_5.py

import turtle

# Funkcja rysująca pojedynczy płatek
def rysuj_platek(promien, kat):
    for _ in range(2):  # Dwa łuki tworzą płatek
        turtle.circle(promien, kat)  # Rysuj łuk
        turtle.left(180 - kat)  # Obrót żółwia, aby ustawić go do rysowania kolejnego łuku

# Funkcja rysująca kwiat
def rysuj_kwiat(liczba_platek, promien, kat_platek):
    kat_obrotu = 360 / liczba_platek  # Kąt obrotu między płatkami
    for _ in range(liczba_platek):
        rysuj_platek(promien, kat_platek)  # Rysuj płatek
        turtle.left(kat_obrotu)  # Obrót żółwia do pozycji kolejnego płatka

    # Rysowanie środka kwiatka
    turtle.penup()
    turtle.goto(0, -promien // 2)  # Przesuń żółwia na środek kwiatka
    turtle.pendown()
    turtle.color("yellow")  # Środek kwiatka w kolorze żółtym
    turtle.begin_fill()
    turtle.circle(promien // 3)  # Narysuj koło jako środek kwiatka
    turtle.end_fill()


turtle.speed("fastest")  # Ustaw szybkość żółwia
turtle.color("red")  # Kolor płatków

liczba_platek = 8  # Liczba płatków
promien_platek = 100  # Promień łuku płatka
kat_platek = 60  # Kąt łuku płatka

rysuj_kwiat(liczba_platek, promien_platek, kat_platek)

turtle.hideturtle()
turtle.done()
