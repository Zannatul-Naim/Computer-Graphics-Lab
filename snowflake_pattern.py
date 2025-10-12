import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size) 
    else:
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)
        t.right(120)
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)
    


def draw_koch_curve(t, order, size):
    for _ in range(4):
        koch_curve(t, order, size)
        t.right(120)


screen = turtle.Screen()

snowflake_turtle = turtle.Turtle()
snowflake_turtle.speed(0)

snowflake_turtle.penup()
snowflake_turtle.goto(-150, 90)
snowflake_turtle.pendown()


draw_koch_curve(snowflake_turtle, 3,300)
turtle.done()