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

# Polygon
polygon = [(-70, -30), (-20, 70), (60, 10), (20, -60)]

def inside(p, edge):
    x, y = p
    if edge == "LEFT": return x >= xmin
    if edge == "RIGHT": return x <= xmax
    if edge == "BOTTOM": return y >= ymin
    if edge == "TOP": return y <= ymax

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    if edge == "LEFT":
        x, y = xmin, y1 + (y2 - y1)*(xmin - x1)/(x2 - x1)
    elif edge == "RIGHT":
        x, y = xmax, y1 + (y2 - y1)*(xmax - x1)/(x2 - x1)
    elif edge == "BOTTOM":
        y, x = ymin, x1 + (x2 - x1)*(ymin - y1)/(y2 - y1)
    elif edge == "TOP":
        y, x = ymax, x1 + (x2 - x1)*(ymax - y1)/(y2 - y1)
    return x, y

def sutherland_hodgman(subject):
    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]
    for edge in edges:
        output = []
        for i in range(len(subject)):
            p1 = subject[i]
            p2 = subject[(i + 1) % len(subject)]
            if inside(p2, edge):
                if not inside(p1, edge):
                    output.append(intersect(p1, p2, edge))
                output.append(p2)
            elif inside(p1, edge):
                output.append(intersect(p1, p2, edge))
        subject = output
    return subject

# Draw window
draw_window()

# Draw original polygon
t.color("blue")
t.penup()
t.goto(polygon[0])
t.pendown()
for p in polygon[1:]:
    t.goto(p)
t.goto(polygon[0])

# Clipped polygon
t.color("red")
clipped = sutherland_hodgman(polygon)
t.penup()
t.goto(clipped[0])
t.pendown()
for p in clipped[1:]:
    t.goto(p)
t.goto(clipped[0])

turtle.done()
