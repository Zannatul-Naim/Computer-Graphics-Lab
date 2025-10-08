import turtle

# Define the points that will shape the curve
control_points = [(-200, 100), (-100, -150), (100, 150), (200, -100)]


screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.color("green")

pen.penup()
# Go through many points along the curve's path (from 0.0 to 1.0)
for i in range(101):
    t = i / 100  # 't' is the position along the path (0% to 100%)
    
    # Calculate the point's position using the De Casteljau's algorithm concept
    # We repeatedly find points between our control points
    p1 = ((1-t) * control_points[0][0] + t * control_points[1][0],
          (1-t) * control_points[0][1] + t * control_points[1][1])
          
    p2 = ((1-t) * control_points[1][0] + t * control_points[2][0],
          (1-t) * control_points[1][1] + t * control_points[2][1])
          
    p3 = ((1-t) * control_points[2][0] + t * control_points[3][0],
          (1-t) * control_points[2][1] + t * control_points[3][1])

    p4 = ((1-t) * p1[0] + t * p2[0],
          (1-t) * p1[1] + t * p2[1])
          
    p5 = ((1-t) * p2[0] + t * p3[0],
          (1-t) * p2[1] + t * p2[1])

    final_point = ((1-t) * p4[0] + t * p5[0],
                   (1-t) * p4[1] + t * p5[1])

    # Move the turtle to the calculated point and draw a dot
    pen.goto(final_point)
    pen.pendown()
    pen.dot(3)
    pen.penup()

pen.color("gray")
pen.width(1)
pen.goto(control_points[0])
pen.pendown()
for point in control_points[1:]:
    pen.goto(point)
pen.penup()

pen.color("red")
for point in control_points:
    pen.goto(point[0], point[1] - 5)
    pen.pendown()
    pen.dot(8)
    pen.penup()

pen.hideturtle()
turtle.done()


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


# WIDTH, HEIGHT = 800, 600
# screen = turtle.Screen()
# screen.setup(WIDTH, HEIGHT)
# screen.title("Bezier Curve")
# screen.bgcolor("white")
# screen.tracer(0)

# pen = turtle.Turtle()
# pen.speed(0)
# pen.width(2)
# pen.color("black")

# draw_axes(WIDTH, HEIGHT)

# control_points = [(27, 243), (101, 47), (324, 197), (437, 23)]
# draw_bezier(control_points, steps=500)

# pen.hideturtle()
# screen.update()
# turtle.done()
