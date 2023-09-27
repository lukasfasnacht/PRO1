import turtle

# User input for different values
font = int(input("Wie dick soll der Stift sein?:"))
color = input("Welche Farbe soll die Blume haben?(green, yellow, blue, lightblue etc.):")
size = int(input("Wie gross sollen die Dreiecke sein?:"))

# Loads Turtle Environment
screen = turtle.Screen()
screen.title('Triangle Flower')
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(font)

# Defines Triangle Function / Draws a 60degree triangle including fill
def triangle(size):
  turtle.begin_fill()
  turtle.fd(size)
  turtle.left(120)
  turtle.fd(size)
  turtle.left(120)
  turtle.fd(size)
  turtle.end_fill()

# Arrangement
turtle.left(30)
turtle.fillcolor(color)
triangle(size)
triangle(size)
triangle(size)

turtle.done()