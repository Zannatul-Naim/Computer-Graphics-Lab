import turtle 
import time 

screen = turtle.Screen()
screen.setup(1000, 800)
screen.setworldcoordinates(0, 0, 1000, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_circle(xc, yc, r):
    x = 0
    y = r 
    p = 1-r 

    t.penup()
    while x<=y:
        t.goto(xc+x, yc+y); t.dot(3)
        t.goto(xc-x, yc-y); t.dot(3)
        t.goto(xc-x, yc+y); t.dot(3)
        t.goto(xc+x, yc-y); t.dot(3)
        t.goto(xc+y, yc+x); t.dot(3)
        t.goto(xc-y, yc-x); t.dot(3)
        t.goto(xc+y, yc-x); t.dot(3)
        t.goto(xc-y, yc+x); t.dot(3)
        time.sleep(0.005)

        if p < 0:
            p = p+2*x+3
        else:
            p = p+2*x-2*y+5
            y -= 1
        x += 1

draw_circle(500, 400, 75)
screen.exitonclick()


# import turtle
# import time

# # Setup
# screen = turtle.Screen()
# screen.title("Bresenham's Circle")
# screen.setup(800, 600)
# screen.setworldcoordinates(0, 0, 800, 600)

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.penup()

# def draw_circle(xc, yc, r):
#     x = 0
#     y = r
#     p = 1 - r  # Initial decision parameter

#     # Loop for the first octant
#     while x <= y:
#         # Plot the 8 symmetric points for the current (x, y)
#         # This is done by adding/subtracting x and y from the center (xc, yc)
#         t.goto(xc + x, yc + y); t.dot(3)
#         t.goto(xc - x, yc + y); t.dot(3)
#         t.goto(xc + x, yc - y); t.dot(3)
#         t.goto(xc - x, yc - y); t.dot(3)
#         t.goto(xc + y, yc + x); t.dot(3)
#         t.goto(xc - y, yc + x); t.dot(3)
#         t.goto(xc + y, yc - x); t.dot(3)
#         t.goto(xc - y, yc - x); t.dot(3)
#         time.sleep(0.1)

#         # Update the decision parameter and coordinates
#         if p < 0:
#             p = p + 2 * x + 3
#         else:
#             p = p + 2 * x - 2 * y + 5
#             y -= 1
#         x += 1

# if __name__ == "__main__":
#     # Draw a few circles to show it works
#     draw_circle(200, 450, 75)
    
#     screen.exitonclick()



    
# import turtle
# import time

# # Setup
# screen = turtle.Screen()
# screen.title("Bresenham's Circle Algorithm")
# screen.setup(800, 600)
# screen.setworldcoordinates(0, 0, 800, 600)
# screen.tracer(0)

# t = turtle.Turtle()
# t.speed(0)
# t.penup()

# def plot_point(x, y, color="black", size=2):
#     t.goto(x, y)
#     t.dot(size, color)
#     screen.update()

# def draw_circle_bresenham(xc, yc, r):
#     x = 0
#     y = r
#     p = 1 - r  # Initial decision parameter

#     print(f"\nDrawing circle at ({xc}, {yc}), radius = {r}")
#     print(f"{'Step':<4} {'X':<4} {'Y':<4} {'P':<6} {'Action'}")
#     print("-" * 30)

#     step = 0

#     def plot_symmetric(x, y):
#         # Plot all 8 symmetric points
#         points = [
#             (x, y), (y, x), (-x, y), (-y, x),
#             (-x, -y), (-y, -x), (x, -y), (y, -x)
#         ]
#         for px, py in points:
#             plot_point(xc + px, yc + py)

#     while x <= y:
#         # Plot current 8 points
#         plot_symmetric(x, y)
#         step += 1

#         if p < 0:
#             action = "E"
#             p = p + 2 * x + 3
#         else:
#             action = "SE"
#             p = p + 2 * x - 2 * y + 5
#             y -= 1
#         x += 1

#         print(f"{step:<4} {x-1:<4} {y:<4} {p:<6} {action}")
#         time.sleep(0.4)  # Visual delay


# if __name__ == "__main__":
#     draw_circle_bresenham(400, 300, 100)  # Center (400,300), radius 100

#     screen.exitonclick()
