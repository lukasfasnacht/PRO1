import turtle

screen = turtle.Screen()
screen.title('Schweizer Fahne')
screen.setup(1000,1000)
turtle.speed(0)
turtle.hideturtle()
turtle.Screen().bgcolor("red")
turtle.color('white')

turtle.up()
turtle.goto(-450,-150)
turtle.down()
turtle.begin_fill()
for _ in range(4):
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(300)
    turtle.left(90)
    turtle.fd(300)
    turtle.left(90)      
turtle.end_fill()
turtle.done()