import turtle

# Loads Turtle Environment
screen = turtle.Screen()
screen.title('Gruppenprojekt')
turtle.speed(0)
# turtle.hideturtle()
turtle.pensize(3)

def Gruppe_P():
  turtle.fd(300)
  turtle.lt(90)
  turtle.fd(400)
  turtle.lt(90)
  turtle.fd(300)
  turtle.lt(90)
  turtle.fd(400)
  turtle.lt(90)
  
  turtle.begin_fill()
  turtle.fillcolor("red")
  turtle.fd(50)
  turtle.left(90)
  turtle.fd(350)
  turtle.right(90)
  turtle.fd(150)
  turtle.right(180)
  turtle.circle(50,-180)
  turtle.right(180)
  turtle.fd(100)
  turtle.right(90)
  turtle.fd(25)
  turtle.right(90)
  turtle.fd(100)
  turtle.left(90)
  turtle.fd(50)
  turtle.left(90)
  turtle.fd(100)
  turtle.left(90)
  turtle.fd(325)
  turtle.end_fill()
  
  
Gruppe_P()

turtle.done()