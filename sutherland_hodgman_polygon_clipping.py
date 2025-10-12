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

# original polygon
polygon = [(300, 350), (500, 200), (700, 350), (500, 500)]

def inside(x, y, edge):
    if edge == 0: return x >= wx1 
    if edge == 1: return y >= wy1 
    if edge == 2: return x <= wx2 
    return y <= wy2 

def intersect(x1, y1, x2, y2, edge):
    dx, dy = x2-x1, y2-y1 

    if edge == 0: t = (wx1-x1)/dx 
    elif edge == 1: t = (wy1-y1)/dy 
    elif edge == 2: t = (wx2-x1)/dx 
    else: t = (wy2-y1)/dy 
    return (x1+t*dx, y1+t*dy)

def clip_edge(points, edge):
    out = []
    x1, y1 = points[-1]
    for x2, y2 in points:
        in1, in2 = inside(x1, y1, edge), inside(x2, y2, edge)
        if in2: 
            if not in1: out.append(intersect(x1, y1, x2, y2, edge))
            out.append((x2, y2))
        elif in1:
            out.append(intersect(x1, y1, x2, y2, edge))
        x1, y1 = x2, y2
    return out

# draw clippint window
t.penup()
t.goto(wx1, wy1)
t.pendown()
t.goto(wx2, wy1), t.goto(wx2, wy2), t.goto(wx1, wy2), t.goto(wx1, wy1)

# draw original polygon
t.color('blue')
t.penup()
t.goto(polygon[0])
t.pendown()
for p in polygon:
    t.goto(p)
t.goto(polygon[0])

# sutherland-hodgman algorithm
clipped = polygon 
for edge in range(4):
    clipped = clip_edge(clipped, edge)

# draw clipped polygon
t.color("green")
t.pensize(3)
t.penup()
t.goto(clipped[0])
t.pendown()
for p in clipped:
    t.goto(p)
    time.sleep(0.5)
t.goto(clipped[0])

screen.exitonclick()