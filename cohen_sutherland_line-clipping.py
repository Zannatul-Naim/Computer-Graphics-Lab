# line_clippping.py

import turtle
import time

screen = turtle.Screen()
screen.title("Line Clipping")
screen.setup(800, 600)
screen.setworldcoordinates(0, 0, 800, 600)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

xmin, ymin = 200, 200
xmax, ymax = 600, 500

TOP, BOTTOM, RIGHT, LEFT = 8, 4, 2, 1

def draw_window():
    t.pencolor("blue")
    t.pensize(2)
    t.goto(xmin, ymin)
    t.pendown()
    for x, y in [(xmax, ymin), (xmax, ymax), (xmin, ymax), (xmin, ymin)]:
        t.goto(x, y)
    t.penup()
    t.goto(400, 520)
    t.write("Clipping Window", align="center", font=("Arial", 12, "bold"))
    screen.update()

def compute_code(x, y):
    code = 0
    if y > ymax: code |= TOP
    elif y < ymin: code |= BOTTOM
    if x > xmax: code |= RIGHT
    elif x < xmin: code |= LEFT
    return code

def clip_line(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2, True  # inside
        elif code1 & code2 != 0:
            return 0, 0, 0, 0, False  # outside

        if code1 != 0:
            code_out, x, y = code1, x1, y1
        else:
            code_out, x, y = code2, x2, y2

        if code_out & TOP:
            x_new = x + (x2 - x1) * (ymax - y) / (y2 - y1)
            y_new = ymax
        elif code_out & BOTTOM:
            x_new = x + (x2 - x1) * (ymin - y) / (y2 - y1)
            y_new = ymin
        elif code_out & RIGHT:
            y_new = y + (y2 - y1) * (xmax - x) / (x2 - x1)
            x_new = xmax
        elif code_out & LEFT:
            y_new = y + (y2 - y1) * (xmin - x) / (x2 - x1)
            x_new = xmin

        # Draw step
        t.goto(x, y)
        t.pendown()
        t.pencolor("orange")
        t.pensize(2)
        t.goto(x_new, y_new)
        t.penup()
        screen.update()
        time.sleep(1)  # pause to show step

        # Update
        if code_out == code1:
            x1, y1, code1 = x_new, y_new, compute_code(x_new, y_new)
        else:
            x2, y2, code2 = x_new, y_new, compute_code(x_new, y_new)

draw_window()

# Original line
x1, y1, x2, y2 = 100, 100, 700, 600
t.goto(x1, y1)
t.pendown()
t.pencolor("gray")
t.pensize(1)
t.goto(x2, y2)
t.penup()
screen.update()
time.sleep(1)

# Clip line with step visualization
new_x1, new_y1, new_x2, new_y2, visible = clip_line(x1, y1, x2, y2)

# Final result
if visible:
    t.goto(new_x1, new_y1)
    t.pendown()
    t.pencolor("red")
    t.pensize(3)
    t.goto(new_x2, new_y2)
    t.penup()
    t.goto((new_x1 + new_x2) / 2, (new_y1 + new_y2) / 2)
    # t.write("Final Clipped Line", align="center", font=("Arial", 10, "bold"))
else:
    t.goto(400, 300)
    # t.write("Line Clipped Out", align="center", font=("Arial", 14, "bold"))

screen.update()
screen.exitonclick()






# import turtle

# screen = turtle.Screen()
# screen.title("Simplified Cohen-Sutherland Line Clipping")
# screen.setup(800, 600)
# screen.setworldcoordinates(0, 0, 800, 600)
# screen.tracer(0)  # For instant drawing

# t = turtle.Turtle()
# t.hideturtle()
# t.speed(0)
# t.penup()

# xmin, ymin = 200, 150
# xmax, ymax = 600, 450

# # Region Codes (using bit flags for efficiency)
# TOP, BOTTOM, RIGHT, LEFT = 8, 4, 2, 1

# def compute_code(x, y):
#     """Generates the 4-bit region code for a point (x, y)."""
#     code = 0
#     if y > ymax: code |= TOP
#     elif y < ymin: code |= BOTTOM
#     if x > xmax: code |= RIGHT
#     elif x < xmin: code |= LEFT
#     return code

# def cohen_sutherland_clip(x1, y1, x2, y2):
#     """
#     Clips a line segment from (x1, y1) to (x2, y2) against the global clipping window.
#     Returns the new endpoints and a boolean indicating if the line is visible.
#     """
#     code1 = compute_code(x1, y1)
#     code2 = compute_code(x2, y2)
#     accept = False

#     while True:
#         # Case 1: Both endpoints are inside the window (trivially accept)
#         if code1 == 0 and code2 == 0:
#             accept = True
#             break
        
#         # Case 2: Both endpoints share an outside region (trivially reject)
#         elif (code1 & code2) != 0:
#             break
        
#         # Case 3: At least one endpoint is outside and needs clipping
#         else:
#             # Pick the outside point
#             if code1 != 0:
#                 code_out = code1
#                 x, y = x1, y1
#             else:
#                 code_out = code2
#                 x, y = x2, y2

#             # Find the intersection point with the window boundary
#             if code_out & TOP:
#                 x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
#                 y = ymax
#             elif code_out & BOTTOM:
#                 x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
#                 y = ymin
#             elif code_out & RIGHT:
#                 y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
#                 x = xmax
#             elif code_out & LEFT:
#                 y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
#                 x = xmin

#             # Update the outside point with the new intersection point
#             if code_out == code1:
#                 x1, y1, code1 = x, y, compute_code(x, y)
#             else:
#                 x2, y2, code2 = x, y, compute_code(x, y)

#     if accept:
#         return x1, y1, x2, y2, True
#     else:
#         return None, None, None, None, False

# def draw_window():
#     """Draws the clipping rectangle."""
#     t.pencolor("blue")
#     t.pensize(2)
#     t.goto(xmin, ymin)
#     t.pendown()
#     t.goto(xmax, ymin)
#     t.goto(xmax, ymax)
#     t.goto(xmin, ymax)
#     t.goto(xmin, ymin)
#     t.penup()
#     screen.update()
# if __name__ == "__main__":
#     draw_window()
    
#     # Original line
#     t.pencolor("gray")
#     t.pensize(1)
#     t.goto(100, 100)
#     t.pendown()
#     t.goto(700, 500)
#     t.penup()
#     screen.update()

#     # Perform clipping
#     new_x1, new_y1, new_x2, new_y2, visible = cohen_sutherland_clip(100, 100, 700, 500)

#     # Draw the final result
#     if visible:
#         t.pencolor("red")
#         t.pensize(3)
#         t.goto(new_x1, new_y1)
#         t.pendown()
#         t.goto(new_x2, new_y2)
#         t.penup()
#         screen.update()

#     screen.exitonclick()
