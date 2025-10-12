import turtle

screen = turtle.Screen()
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.goto(300, 600)
t.pendown()

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size) 
    else:
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)
        t.right(120)
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)

def draw_koch_curve(t, order, size):
    for _ in range(4):
        koch_curve(t, order, size)
        t.right(120)

draw_koch_curve(t, 5, 500)

screen.exitonclick()