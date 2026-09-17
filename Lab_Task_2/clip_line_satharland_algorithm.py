import turtle

t = turtle.Turtle()
t.speed(3)

xmin, ymin, xmax, ymax = -50, -50, 50, 50

def draw_window():
    t.penup()
    t.goto(xmin, ymin)
    t.pendown()
    for _ in range(2):
        t.forward(xmax - xmin)
        t.left(90)
        t.forward(ymax - ymin)
        t.left(90)

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def code(x, y):
    c = INSIDE
    if x < xmin: c |= LEFT
    elif x > xmax: c |= RIGHT
    if y < ymin: c |= BOTTOM
    elif y > ymax: c |= TOP
    return c

def cohen_sutherland(x1, y1, x2, y2):
    c1, c2 = code(x1, y1), code(x2, y2)
    while True:
        if not (c1 | c2):
            return (x1, y1, x2, y2)
        elif c1 & c2:
            return None
        else:
            out = c1 or c2
            if out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            if out == c1:
                x1, y1, c1 = x, y, code(x, y)
            else:
                x2, y2, c2 = x, y, code(x, y)
    return None

# Draw window
draw_window()

# Line
x1, y1, x2, y2 = -80, 0, 80, 0
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)

clipped = cohen_sutherland(x1, y1, x2, y2)
if clipped:
    t.color("red")
    t.penup()
    t.goto(clipped[0], clipped[1])
    t.pendown()
    t.goto(clipped[2], clipped[3])
turtle.done()
