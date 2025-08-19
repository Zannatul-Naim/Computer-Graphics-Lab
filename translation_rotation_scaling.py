import turtle
import math
import time

screen = turtle.Screen()
screen.title("Program 3: 2D Transformations")
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.penup()

def draw_shape(points, color, label):
    t.pencolor(color)
    t.pensize(3)
    t.penup()
    for i, (x, y) in enumerate(points):
        t.goto(x, y)
        t.dot(4, color)
        if i == 0:
            t.pendown()
        else:
            t.goto(x, y)
    t.goto(points[0])
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    # t.penup()
    # t.goto(cx, cy - 15)
    # t.color("purple")
    # t.write(label, align="center", font=("Arial", 10, "bold"))
    screen.update()

def translate_point(x, y, tx, ty):
    return x + tx, y + ty

def rotate_point(x, y, angle_deg, cx, cy):
    rad = math.radians(angle_deg)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    x -= cx
    y -= cy
    x_new = x * cos_a - y * sin_a
    y_new = x * sin_a + y * cos_a
    return x_new + cx, y_new + cy

def scale_point(x, y, sx, sy, cx, cy):
    x -= cx
    y -= cy
    x_new = x * sx
    y_new = y * sy
    return x_new + cx, y_new + cy

# Define triangle
original = [(-40, -40), (40, -40), (0, 60)]
base_x, base_y = 300, 300
triangle = [(x + base_x, y + base_y) for x, y in original]

cx = sum(p[0] for p in triangle) / 3
cy = sum(p[1] for p in triangle) / 3

print("=== 2D TRANSFORMATIONS LAB ===")
print(f"Center of triangle: ({cx:.1f}, {cy:.1f})")

# Draw original
draw_shape(triangle, "black", "Original")
time.sleep(1.5)

# Translate
translated = [translate_point(x, y, 200, 0) for x, y in triangle]
draw_shape(translated, "green", "Translated")
print("Applied: Translation (200, 0)")
time.sleep(1.5)

# Rotate
rotated = [rotate_point(x, y, 45, cx + 200, cy) for x, y in translated]
draw_shape(rotated, "red", "Rotated 45°")
print("Applied: Rotation about center")
time.sleep(1.5)

# Scale
scaled = [scale_point(x, y, 1.5, 1.5, cx + 200, cy) for x, y in rotated]
draw_shape(scaled, "blue", "Scaled 1.5x")
print("Applied: Uniform scaling")

screen.exitonclick()