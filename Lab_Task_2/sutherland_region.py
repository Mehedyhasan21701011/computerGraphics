import turtle

t = turtle.Turtle()
t.speed(3)

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

# Region code function
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def code(x, y):
    c = INSIDE
    if x < xmin: c |= LEFT
    elif x > xmax: c |= RIGHT
    if y < ymin: c |= BOTTOM
    elif y > ymax: c |= TOP
    return f"{c:04b}"

points = [(-70, -70), (0, 0), (70, 70), (70, 0), (0, 70)]
for x, y in points:
    t.penup()
    t.goto(x, y)
    t.dot(10, "red")
    t.write(code(x, y))

turtle.done()
