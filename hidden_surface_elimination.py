import turtle

# Setup 
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Hidden Surface Elimination")

pen = turtle.Turtle()
pen.speed(0) # Set to fastest for drawing
pen.pensize(2)
pen.color("black")

# Draw Main Axes 
def draw_axes():
    # X-axis
    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()
    pen.goto(300, 0)
    # Y-axis
    pen.penup()
    pen.goto(0, -300)
    pen.pendown()
    pen.goto(0, 300)

# Draw Triangle
def drawTriangle():
    x = [10, 50, 100]
    y = [100, 20, 100]

    pen.penup()
    pen.goto(x[0], y[0])
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.goto(x[1], y[1])
    pen.goto(x[2], y[2])
    pen.goto(x[0], y[0])
    pen.end_fill()

# Draw Circle
def drawCircle():
    pen.penup()
    pen.goto(100, 55)  
    pen.pendown()
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(45)
    pen.end_fill()

# Draw Rectangle
def drawRectangle():
    x1, y1 = 40, 90
    x2, y2 = 120, 180

    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.goto(x2, y1)
    pen.goto(x2, y2)
    pen.goto(x1, y2)
    pen.goto(x1, y1)
    pen.end_fill()
    

shapes_to_draw = [
    ("T", 30),
    ("R", 10),
    ("C", 10),
]

sorted_shapes = sorted(shapes_to_draw, key=lambda s: s[1], reverse=True)

draw_axes()

for shape_name, depth in sorted_shapes:
    if shape_name == "C":
        drawCircle()
    elif shape_name == "T":
        drawTriangle()
    elif shape_name == "R":
        drawRectangle()
        
pen.hideturtle()
turtle.done()