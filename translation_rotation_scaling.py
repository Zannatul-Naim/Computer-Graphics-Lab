import turtle 
import time 
import math

screen = turtle.Screen()
screen.title("2D Transformation")
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

t = turtle.Turtle()
t.speed(0)
t.penup()

def draw_shape(points, color):
    t.pencolor(color)
    t.pensize(3)
    t.penup()
    t.goto(points[0])
    t.pendown()

    for x, y in points[1:]:
        t.goto(x, y)
        t.dot(4, color)
    t.goto(points[0])
    screen.update()

def translate_points(points, tx, ty):
    new_points = []
    for x, y in points:
        new_points.append((x+tx, y+ty))
    return new_points

def scale_points(points, sx, sy, cx, cy):
    new_points = []
    for x, y in points:
        x_new = (x-cx)*sx + cx
        y_new = (y-cy)*sy + cy 
        new_points.append((x_new, y_new))
    return new_points 

def rotate_points(points, angle_deg, cx, cy):
    rad = math.radians(angle_deg)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    new_points = []
    for x, y in points:
        x_temp = x-cx 
        y_temp = y-cy 
        x_new = x_temp*cos_a - y_temp*sin_a 
        y_new = x_temp*sin_a + y_temp*cos_a

        new_points.append((x_new+cx, y_new+cy))
    return new_points

t.pencolor("lightgray")
t.pensize(1)
t.pendown()
t.goto(0, 400), t.goto(1000, 400)  # X-axis
t.penup(), t.goto(500, 0), t.pendown(), t.goto(500, 800)  # Y-axis
t.penup()

original = [(-40, -40), (40, -40), (0, 0)]
base_x, base_y = 500, 400
triangle = []
for x, y in original:
    triangle.append((x+base_x, y+base_y))

draw_shape(triangle, "black")
time.sleep(1.5)

# translate
translated_points = translate_points(triangle, 100, 100)
draw_shape(translated_points, "green")
time.sleep(1)

# calculate center
cx = sum(p[0] for p in triangle) / 3
cy = sum(p[1] for p in triangle) / 3

scaled_points = scale_points(translated_points, 2, 2, cx+100, cy+100)
draw_shape(scaled_points, "red")
time.sleep(1)

rotated_points = rotate_points(scaled_points, 90, cx+100, cy+100)
draw_shape(rotated_points, "blue")
time.sleep(1)

screen.exitonclick()