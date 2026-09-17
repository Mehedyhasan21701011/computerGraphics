import turtle

t = turtle.Turtle()
t.speed(3)

def draw_chair(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.left(90)

    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.right(90)
    t.right(90)



# Original
draw_chair(-100, 0)
# Translate to new coordinate
draw_chair(100, 0)

turtle.done()
