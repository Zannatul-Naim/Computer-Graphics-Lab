import turtle
import time

# Setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.setworldcoordinates(0, 0, 800, 600)
screen.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Clipping window
xmin, ymin = 200, 200
xmax, ymax = 600, 500

# Region codes
TOP, BOTTOM, RIGHT, LEFT = 8, 4, 2, 1

def compute_code(x, y):
    code = 0
    if y > ymax: code |= TOP
    elif y < ymin: code |= BOTTOM
    if x > xmax: code |= RIGHT
    elif x < xmin: code |= LEFT
    return code

def clip_line(x1, y1, x2, y2):
    code1, code2 = compute_code(x1, y1), compute_code(x2, y2)
    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2, True
        elif code1 & code2 != 0:
            return 0, 0, 0, 0, False
        
        code_out = code1 if code1 != 0 else code2
        x, y = (x1, y1) if code_out == code1 else (x2, y2)
        
        if code_out & TOP:
            x_new = x + (x2 - x1) * (ymax - y) / (y2 - y1)
            y_new = ymax
        elif code_out & BOTTOM:
            x_new = x + (x2 - x1) * (ymin - y) / (y2 - y1)
            y_new = ymin
        elif code_out & RIGHT:
            y_new = y + (y2 - y1) * (xmax - x) / (x2 - x1)
            x_new = xmax
        else:
            y_new = y + (y2 - y1) * (xmin - x) / (x2 - x1)
            x_new = xmin
        
        # Show clipping step
        t.color("red")
        t.width(2)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x_new, y_new)
        screen.update()
        time.sleep(0.8)
        
        if code_out == code1:
            x1, y1, code1 = x_new, y_new, compute_code(x_new, y_new)
        else:
            x2, y2, code2 = x_new, y_new, compute_code(x_new, y_new)

# Draw clipping window
t.color("blue")
t.width(2)
t.penup()
t.goto(xmin, ymin)
t.pendown()
for x, y in [(xmax, ymin), (xmax, ymax), (xmin, ymax), (xmin, ymin)]:
    t.goto(x, y)
screen.update()

# Original line
x1, y1, x2, y2 = 100, 100, 500, 300
t.color("gray")
t.width(1)
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)
screen.update()
time.sleep(1)

# Cohen-Sutherland clipping with steps
new_x1, new_y1, new_x2, new_y2, visible = clip_line(x1, y1, x2, y2)

# Draw final clipped line
if visible:
    t.color("green")
    t.width(3)
    t.penup()
    t.goto(new_x1, new_y1)
    t.pendown()
    t.goto(new_x2, new_y2)
    screen.update()

turtle.done()