import turtle

# Setup
screen = turtle.Screen()
screen.setup(600, 500)
screen.setworldcoordinates(0, 0, 500, 400)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Clipping window
clip_x1, clip_y1 = 100, 100
clip_x2, clip_y2 = 300, 300

# Original polygon
polygon = [(150, 150), (250, 80), (350, 200), (280, 320), (120, 280)]

def inside(x, y, edge):
    if edge == 0: return x >= clip_x1
    if edge == 1: return y >= clip_y1
    if edge == 2: return x <= clip_x2
    return y <= clip_y2

def intersect(x1, y1, x2, y2, edge):
    dx, dy = x2 - x1, y2 - y1
    if edge == 0: t = (clip_x1 - x1) / dx
    elif edge == 1: t = (clip_y1 - y1) / dy
    elif edge == 2: t = (clip_x2 - x1) / dx
    else: t = (clip_y2 - y1) / dy
    return (x1 + t * dx, y1 + t * dy)

def clip_edge(pts, edge):
    out = []
    x1, y1 = pts[-1]
    for x2, y2 in pts:
        in1, in2 = inside(x1, y1, edge), inside(x2, y2, edge)
        if in2:
            if not in1: out.append(intersect(x1, y1, x2, y2, edge))
            out.append((x2, y2))
        elif in1:
            out.append(intersect(x1, y1, x2, y2, edge))
        x1, y1 = x2, y2
    return out

# Sutherland-Hodgman algorithm
clipped = polygon
for e in range(4):
    clipped = clip_edge(clipped, e)

# Draw clipping window
t.color("red")
t.penup()
t.goto(clip_x1, clip_y1)
t.pendown()
for pos in [(clip_x2, clip_y1), (clip_x2, clip_y2), (clip_x1, clip_y2), (clip_x1, clip_y1)]:
    t.goto(pos)

# Draw original polygon
t.color("blue")
t.penup()
t.goto(polygon[0])
t.pendown()
for p in polygon:
    t.goto(p)
t.goto(polygon[0])

# Draw clipped polygon
t.color("green")
t.width(3)
t.penup()
t.goto(clipped[0])
t.pendown()
for p in clipped:
    t.goto(p)
t.goto(clipped[0])

turtle.done()