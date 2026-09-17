import turtle

t = turtle.Turtle()
t.speed(3)

def midpoint_line(x1, y1, x2, y2):
    if abs(x2 - x1) < 2 and abs(y2 - y1) < 2:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
        return
    xm, ym = (x1 + x2)/2, (y1 + y2)/2
    midpoint_line(x1, y1, xm, ym)
    midpoint_line(xm, ym, x2, y2)

midpoint_line(-100, -50, 100, 50)
turtle.done()
