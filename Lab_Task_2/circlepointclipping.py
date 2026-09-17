import turtle
import math

t = turtle.Turtle()
t.speed(3)

# Circle clipping window
xc, yc = 0, 0
r = 100

# Draw circular window
t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)

# Points to test
points = [(-50, 0), (80, 50), (120, 0), (0, 90), (0,0),(0, 150) ]

# Function to check whether a point is inside the circle
def inside_circle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2

# Draw points and mark them
for x, y in points:
    t.penup()
    t.goto(x, y)
    if inside_circle(x, y, xc, yc, r):
        t.dot(10, "green")
        t.write(" Inside", font=("Arial", 10, "normal"))
    else:
        t.dot(10, "red")
        t.write(" Outside", font=("Arial", 10, "normal"))

t.hideturtle()
turtle.done()
