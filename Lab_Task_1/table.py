import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Table Drawing")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

# Function to draw rectangle
def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# -------- Draw Table --------
# Tabletop
draw_rectangle(-150, 100, 300, 30, "saddlebrown")

# Table legs (front two)
draw_rectangle(-140, 70, 20, 100, "peru")     # left front leg
draw_rectangle(120, 70, 20, 100, "peru")      # right front leg

# Table legs (back two - slightly shorter)
draw_rectangle(-100, 70, 15, 80, "burlywood")  # left back leg
draw_rectangle(85, 70, 15, 80, "burlywood")    # right back leg

# Crossbar under table
draw_rectangle(-100, 40, 185, 10, "darkgoldenrod")

# Hide turtle
pen.hideturtle()

turtle.done()
