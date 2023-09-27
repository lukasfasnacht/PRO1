import turtle

# User input for different values
font = int(input("Wie dick soll der Stift sein?:"))
color_1 = input("Welche Farbe soll die erste Blume haben?(green, yellow, blue, lightblue etc.):")
color_2 = input("Welche Farbe soll die zweite Blume haben?(green, yellow, blue, lightblue etc.):")
color_3 = input("Welche Farbe soll die dritte Blume haben?(green, yellow, blue, lightblue etc.):")
color_4 = input("Welche Farbe soll die vierte Blume haben?(green, yellow, blue, lightblue etc.):")
color_5 = input("Welche Farbe soll die fünfte Blume haben?(green, yellow, blue, lightblue etc.):")
size = int(input("Wie gross sollen die Dreiecke sein?:"))

# Loads Turtle Environment
screen = turtle.Screen()
screen.title('Square Flower')
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(font)

# Defines Square Function / Draws a perfect square including fill
def square(size):
  turtle.begin_fill()
  turtle.fd(size)
  turtle.left(90)
  turtle.fd(size)
  turtle.left(90)
  turtle.fd(size)
  turtle.left(90)
  turtle.fd(size)
  turtle.end_fill()

# Arrangement
turtle.right(45)
turtle.fillcolor(color_1)
square(size)
turtle.left(18)
turtle.fillcolor(color_2)
square(size)
turtle.left(18)
turtle.fillcolor(color_3)
square(size)
turtle.left(18)
turtle.fillcolor(color_4)
square(size)
turtle.left(18)
turtle.fillcolor(color_5)
square(size)

turtle.done()