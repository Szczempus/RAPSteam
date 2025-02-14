import turtle

liczba_bokow = int(input("Podaj liczbę boków wielokąta: "))

t = turtle.Turtle()

kat = 360 / liczba_bokow

for _ in range(liczba_bokow):
    t.forward(100) 
    t.right(kat)

turtle.done()