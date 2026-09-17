import turtle

t = turtle.Turtle()

# Line endpoints
x1, y1 = -100, -50
x2, y2 = 100, 50
# Test point
px, py = 50, 0

# Draw line
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)

# Draw point
t.penup()
t.goto(px, py)
t.dot(10, "red")
t.penup()

# Check position
val = (x2 - x1)*(py - y1) - (y2 - y1)*(px - x1)
if val > 0:
    t.write("Point is LEFT of the line.", font=("Arial", 12, "normal"))
elif val < 0:
    t.write("Point is right of the line.", font=("Arial", 12, "normal"))
else:
    t.write("Point is on the line.", font=("Arial", 12, "normal"))

turtle.done()
