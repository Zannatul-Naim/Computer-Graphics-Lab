import turtle 
import time 

screen = turtle.Screen()
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# clipping window
wx1, wy1 = 350, 250
wx2, wy2 = 650, 450

# region codes
TOP, BOTTOM, RIGHT, LEFT = 8, 4, 2, 1

def compute_code(x, y):
    code = 0
    if y > wy2: code |= TOP 
    elif y < wy1: code |= BOTTOM
    if x > wx2: code |= RIGHT
    elif x < wx1: code |= LEFT
    return code 

def clip_line(x1, y1, x2, y2):
    code1, code2 = compute_code(x1, y1), compute_code(x2, y2)
    while True: 
        if code1|code2 == 0:
            return x1, y1, x2, y2, True
        elif code1&code2 != 0:
            return 0, 0, 0, 0, False 
        code_out = code1 if code1 != 0 else code2 
        x, y = (x1, y1) if code_out == code1 else (x2, y2)

        if code_out & TOP: 
            x_new = x + (x2-x1) * (wy2-y)/(y2-y1)
            y_new = wy2
        elif code_out & BOTTOM:
            x_new = x + (x2-x1) * (wy1-y)/(y2-y1)
            y_new = wy1
        elif code_out & RIGHT: 
            y_new = y + (y2-y1)*(wx2-x)/(x2-x1)
            x_new = wx2 
        else:
            y_new = y + (y2-y1)*(wx1-x)/(x2-x1)
            x_new = wx1

        # show clipping steps
        t.color("red")
        t.width(2)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x_new, y_new)
        time.sleep(1)

        if code_out == code1:
            x1, y1, code1 = x_new, y_new, compute_code(x_new, y_new)
        else:
            x2, y2, code2 = x_new, y_new, compute_code(x_new, y_new)



# window
t.penup()
t.goto(wx1, wy1)
t.pendown()
t.goto(wx2, wy1)
t.goto(wx2, wy1), t.goto(wx2, wy2), t.goto(wx1, wy2), t.goto(wx1, wy1)

# original line
x1, y1, x2, y2 = 300, 260, 700, 440
t.color("blue")
t.width(2)
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)

new_x1, new_y1, new_x2, new_y2, visible = clip_line(x1, y1, x2, y2)

if visible:
    t.color("green")
    t.width(3)
    t.penup()
    t.goto(new_x1, new_y1)
    t.pendown()
    t.goto(new_x2, new_y2)

screen.exitonclick()