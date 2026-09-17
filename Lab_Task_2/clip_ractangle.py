import turtle

t = turtle.Turtle()
t.speed(3)

# Window
xmin, ymin, xmax, ymax = -50, -50, 50, 50

# Draw window
t.penup()
t.goto(xmin, ymin)
t.pendown()
for _ in range(2):
    t.forward(xmax - xmin)
    t.left(90)
    t.forward(ymax - ymin)
    t.left(90)

# Points
points = [(-70, 0), (0, 0), (60, 60), (30, -30)]
for x, y in points:
    if xmin <= x <= xmax and ymin <= y <= ymax:
        t.penup()
        t.goto(x, y)
        t.dot(10, "green")
    else:
        t.penup()
        t.goto(x, y)
        t.dot(10, "red")

turtle.done()
