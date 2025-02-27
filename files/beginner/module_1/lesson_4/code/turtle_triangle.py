import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Triangle")

# Create a turtle named "triangle_turtle"
triangle_turtle = turtle.Turtle()

# Draw a triangle
for _ in range(3):
    triangle_turtle.forward(100)  # Move forward by 100 units
    triangle_turtle.left(120)     # Turn left by 120 degrees

# Hide the turtle and display the window
triangle_turtle.hideturtle()
turtle.done()