import turtle
import math

# Compute binomial coefficient nCk in a simple way
def binomial(n, k):
    return math.comb(n, k)  # Python 3.8+

# Bernstein basis
def bernstein(n, k, u):
    return binomial(n, k) * (u**k) * ((1-u)**(n-k))

def draw_bezier(points, steps=500):
    n = len(points) - 1
    pen.color("green")
    pen.penup()

    # Draw curve
    for i in range(steps+1):
        u = i / steps
        x = y = 0
        for k in range(n+1):
            b = bernstein(n, k, u)
            x += points[k][0]*b
            y += points[k][1]*b
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)

    # Draw control points
    pen.penup()
    pen.color("red")
    for px, py in points:
        pen.goto(px, py-3)
        pen.pendown()
        pen.circle(3)
        pen.penup()

    # Draw control polygon
    pen.color("gray")
    pen.goto(points[0])
    pen.pendown()
    for (px, py) in points[1:]:
        pen.goto(px, py)
    pen.penup()

def draw_axes(width, height):
    pen.penup()
    pen.goto(-width/2, 0)
    pen.pendown()
    pen.goto(width/2, 0)
    pen.write("X")

    pen.penup()
    pen.goto(0, -height/2)
    pen.pendown()
    pen.goto(0, height/2)
    pen.write("Y")
    pen.penup()


WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Bezier Curve")
screen.bgcolor("white")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.color("black")

draw_axes(WIDTH, HEIGHT)

control_points = [(27, 243), (101, 47), (324, 197), (437, 23)]
draw_bezier(control_points, steps=500)

pen.hideturtle()
screen.update()
turtle.done()
