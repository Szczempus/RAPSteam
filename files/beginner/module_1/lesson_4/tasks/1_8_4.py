# Zadanie: 1_8_4.py

import turtle

spiral = turtle.Turtle()

step_length = 10

for _ in range(20):
    spiral.forward(step_length)  
    spiral.left(30)             
    step_length += 5           


turtle.done()