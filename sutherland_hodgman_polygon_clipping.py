import turtle

# Define a Point structure
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Global variables
polygon = []
clipped = []
clipMin = Point(100, 100)
clipMax = Point(300, 300)

# Initialize screen
screen = turtle.Screen()
screen.title("Sutherland-Hodgeman Polygon Clipping")
screen.setup(600, 500)
screen.setworldcoordinates(0, 0, 500, 400)
screen.tracer(0)  # Fast drawing

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def inside(p, edge):
    # Check if point p is inside wrt edge
    if edge == 0: return p.x >= clipMin.x       # left
    if edge == 1: return p.y >= clipMin.y       # bottom
    if edge == 2: return p.x <= clipMax.x       # right
    if edge == 3: return p.y <= clipMax.y       # top

def intersect(p1, p2, edge):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    tval = 0
    if edge == 0:    # left
        tval = (clipMin.x - p1.x)/dx
    elif edge == 1:  # bottom
        tval = (clipMin.y - p1.y)/dy
    elif edge == 2:  # right
        tval = (clipMax.x - p1.x)/dx
    elif edge == 3:  # top
        tval = (clipMax.y - p1.y)/dy
    return Point(p1.x + tval*dx, p1.y + tval*dy)

def clipEdge(inp, edge):
    outp = []
    if not inp:
        return outp
    s = inp[-1]
    for p in inp:
        if inside(p, edge):
            if not inside(s, edge):
                outp.append(intersect(s, p, edge))
            outp.append(p)
        elif inside(s, edge):
            outp.append(intersect(s, p, edge))
        s = p
    return outp

def clipPolygon():
    global clipped
    clipped = polygon.copy()
    for e in range(4):
        clipped = clipEdge(clipped, e)
    print("Clipped polygon has", len(clipped), "vertices")
    redraw()

def draw_polygon(points, color="blue", thick=1):
    if not points:
        return
    t.color(color)
    t.width(thick)
    t.penup()
    t.goto(points[0].x, points[0].y)
    t.pendown()
    for p in points:
        t.goto(p.x, p.y)
    t.goto(points[0].x, points[0].y)
    t.penup()
    t.width(1)

def draw_window():
    t.color("red")
    t.penup()
    t.goto(clipMin.x, clipMin.y)
    t.pendown()
    t.goto(clipMax.x, clipMin.y)
    t.goto(clipMax.x, clipMax.y)
    t.goto(clipMin.x, clipMax.y)
    t.goto(clipMin.x, clipMin.y)
    t.penup()

def redraw():
    t.clear()
    # original polygon
    draw_polygon(polygon, "blue")
    # clipping window
    draw_window()
    # clipped polygon
    draw_polygon(clipped, "green", 3)
    screen.update()

def click(x, y):
    polygon.append(Point(x, y))
    print(f"Added point: ({x:.1f}, {y:.1f})")
    redraw()

def keypress_c():
    clipPolygon()

def keypress_r():
    polygon.clear()
    clipped.clear()
    redraw()

# Setup instructions
print("Instructions:")
print("- Left click to add polygon points")
print("- Press 'c' to clip")
print("- Press 'r' to reset")
print("- Close the window to exit")

# Bindings
screen.onclick(click)
screen.onkey(keypress_c, "c")
screen.onkey(keypress_r, "r")
screen.listen()

# Initial draw
redraw()
turtle.done()
