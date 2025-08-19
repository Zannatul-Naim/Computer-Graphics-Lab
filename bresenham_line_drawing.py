# bresenham_line_drawing.py

import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.title("Bresenham's Line Algorithm")
screen.setup(800, 600)
screen.setworldcoordinates(0, 0, 800, 600)
screen.tracer(0)  # Manual update

t = turtle.Turtle()
t.speed(0)
t.penup()

def plot_point(x, y, color="black", size=3):
    t.goto(x, y)
    t.dot(size, color)
    screen.update()  # Show immediately

def draw_line_bresenham_full(x1, y1, x2, y2):
    # Store original inputs for reference
    orig_x1, orig_y1, orig_x2, orig_y2 = x1, y1, x2, y2

    # Compute differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine step direction
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    # Check if line is steep (|dy| > |dx|)
    swapped = False
    if dy > dx:
        # Swap x and y roles
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
        sx, sy = sy, sx
        swapped = True

    # Initial decision parameter
    p = 2 * dy - dx

    x, y = x1, y1

    # Print header
    print(f"\nDrawing line from ({orig_x1}, {orig_y1}) to ({orig_x2}, {orig_y2})")
    print(f"{'Step':<4} {'RawX':<6} {'RawY':<6} {'P':<6} {'Action'}")
    print("-" * 30)

    # Plot first point
    plot_x = y if swapped else x
    plot_y = x if swapped else y
    plot_point(plot_x, plot_y)
    print(f"{1:<4} {plot_x:<6} {plot_y:<6} {'-':<6} Started")

    step = 1

    # Main loop: step in x-direction (now guaranteed dx >= dy)
    for i in range(dx):
        x += sx
        step += 1

        if p < 0:
            p = p + 2 * dy
            action = "E" if not swapped else "N"
        else:
            y += sy
            p = p + 2 * dy - 2 * dx
            action = "NE" if not swapped else "NE (swap)"

        # Unswap coordinates for plotting
        plot_x = y if swapped else x
        plot_y = x if swapped else y

        plot_point(plot_x, plot_y)
        print(f"{step:<4} {plot_x:<6} {plot_y:<6} {p:<6} {action}")

        time.sleep(0.1)  # Delay to visualize

if __name__ == "__main__":
    # Try different types of lines

    # Shallow positive slope (original case)
    # draw_line_bresenham_full(100, 100, 700, 300)

    # Steep positive slope (was broken before!)
    # draw_line_bresenham_full(100, 100, 200, 500)

    # Negative slope (shallow)
    draw_line_bresenham_full(100, 500, 700, 100)

    # Horizontal line
    # draw_line_bresenham_full(100, 300, 700, 300)

    # # Vertical line
    # draw_line_bresenham_full(400, 100, 400, 500)

    screen.exitonclick()

