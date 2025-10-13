import turtle 
import time 

# control_points = [(-300, 0), (-150, 200), (0, -200), (150, 200), (300, 0)]
control_points = [(400,400), (425,350), (475, 450), (525, 350), (575, 450), (600, 400)]

screen = turtle.Screen()
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

t = turtle.Turtle()
t.speed(0)
t.penup()

def draw_axes(width, height):
    t.penup()
    t.goto(10, height/2)
    t.pendown()
    t.goto(width-10, height/2)
    t.write("X")

    t.penup()
    t.goto(width/2, 10)
    t.pendown()
    t.goto(width/2, height-10)
    t.write("Y")
    t.penup()
draw_axes(1000, 800)

for i in range(101):
    
    ti = i/100

    points = control_points.copy()

    while len(points)>1:
        new_points = []
        for i in range(len(points)-1):
            x = (1-ti)*points[i][0] + ti*points[i+1][0]
            y = (1-ti)*points[i][1] + ti*points[i+1][1]
            new_points.append((x, y))
        points = new_points 
    
    t.goto(points[0])
    t.pendown()

# draw control line and points
t.color("blue")
t.penup()
t.goto(control_points[0])
t.pendown()
for p in control_points[1:]:
    t.goto(p)

t.color("red")
t.penup()
for p in control_points:
    t.goto(p)
    t.dot(5)

t.hideturtle()
screen.exitonclick()


# import turtle
# import math

# # Compute binomial coefficient nCk in a simple way
# def binomial(n, k):
#     return math.comb(n, k)  # Python 3.8+

# # Bernstein basis
# def bernstein(n, k, u):
#     return binomial(n, k) * (u**k) * ((1-u)**(n-k))

# def draw_bezier(points, steps=500):
#     n = len(points) - 1
#     pen.color("green")
#     pen.penup()

#     # Draw curve
#     for i in range(steps+1):
#         u = i / steps
#         x = y = 0
#         for k in range(n+1):
#             b = bernstein(n, k, u)
#             x += points[k][0]*b
#             y += points[k][1]*b
#         if i == 0:
#             pen.goto(x, y)
#             pen.pendown()
#         else:
#             pen.goto(x, y)

#     # Draw control points
#     pen.penup()
#     pen.color("red")
#     for px, py in points:
#         pen.goto(px, py-3)
#         pen.pendown()
#         pen.circle(3)
#         pen.penup()

#     # Draw control polygon
#     pen.color("gray")
#     pen.goto(points[0])
#     pen.pendown()
#     for (px, py) in points[1:]:
#         pen.goto(px, py)
#     pen.penup()

# def draw_axes(width, height):
#     pen.penup()
#     pen.goto(-width/2, 0)
#     pen.pendown()
#     pen.goto(width/2, 0)
#     pen.write("X")

#     pen.penup()
#     pen.goto(0, -height/2)
#     pen.pendown()
#     pen.goto(0, height/2)
#     pen.write("Y")
#     pen.penup()


# WIDTH, HEIGHT = 1000, 800
# screen = turtle.Screen()
# screen.setup(WIDTH, HEIGHT)
# screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
# screen.title("Bezier Curve")
# screen.bgcolor("white")
# screen.tracer(0)

# pen = turtle.Turtle()
# pen.speed(0)
# pen.width(2)
# pen.color("black")

# draw_axes(WIDTH, HEIGHT)

# # control_points = [(27, 243), (101, 47), (324, 197), (437, 23)]
# control_points = [(400,400), (425,350), (475, 450), (525, 350), (575, 450), (600, 400)]
# draw_bezier(control_points, steps=500)

# pen.hideturtle()
# screen.update()
# turtle.done()
