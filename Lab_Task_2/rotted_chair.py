import turtle
import math

t = turtle.Turtle()
t.speed(1)
t.pensize(2)

# Chair shape (a rectangle seat + backrest)
# Coordinates are relative to (0, 0)
chair = [
    (0, 0), (60, 0), (60, 20), (0, 20),  # Seat
    (0, 20), (0, 80), (10, 80), (10, 20),(0,20),(0,0)  # Backrest
]

angle = 45  # degrees
rad = math.radians(angle)

# Rotation function
def rotate_point(x, y, cx, cy):
    x -= cx
    y -= cy
    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)
    return xr + cx, yr + cy

# Draw shape
def draw_shape(points, color):
    t.color(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.penup()

# Draw original chair
draw_shape(chair, "black")

# Rotate chair 45° around origin (0, 0)
rotated_chair = [rotate_point(x, y, 0, 0) for x, y in chair]
draw_shape(rotated_chair, "red")

# Add labels
t.penup()
t.goto(-20, -10)
t.color("black")
t.write("Original", font=("Arial", 12, "normal"))
t.goto(40, 40)
t.color("red")
t.write("Rotated 45°", font=("Arial", 12, "normal"))

t.hideturtle()
turtle.done()
