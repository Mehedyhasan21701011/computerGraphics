import turtle
import math

t = turtle.Turtle()
t.speed(3)

# Circle window
cx, cy, r = 0, 0, 50

t.penup()
t.goto(0, -r)
t.pendown()
t.circle(r)

# Line
x1, y1, x2, y2 = -100, 0, 100, 0
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)

# Clip
dx, dy = x2 - x1, y2 - y1
a = dx**2 + dy**2
b = 2*(x1*dx + y1*dy)
c = x1**2 + y1**2 - r**2
disc = b**2 - 4*a*c

if disc >= 0:
    t.color("red")
    t.penup()
    t1 = (-b - math.sqrt(disc)) / (2*a)
    t2 = (-b + math.sqrt(disc)) / (2*a)
    x_start, y_start = x1 + dx*t1, y1 + dy*t1
    x_end, y_end = x1 + dx*t2, y1 + dy*t2
    t.goto(x_start, y_start)
    t.pendown()
    t.goto(x_end, y_end)

turtle.done()
