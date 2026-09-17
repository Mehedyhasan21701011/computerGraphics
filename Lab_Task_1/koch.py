import turtle

def koch_curve(t, order, length):
    if order == 0:
        t.forward(length)
    else:
        koch_curve(t, order-1, length/3)
        t.left(60)
        koch_curve(t, order-1, length/3)
        t.right(120)
        koch_curve(t, order-1, length/3)
        t.left(60)
        koch_curve(t, order-1, length/3)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # fastest drawing

t.penup()
t.goto(-200, 0)
t.pendown()

# Draw Koch curve of order 3
koch_curve(t, 3, 300)

screen.mainloop()
