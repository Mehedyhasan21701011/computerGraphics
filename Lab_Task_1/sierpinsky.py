import turtle

def sierpinski(t, order, length):
    if order == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(t, order-1, length/2)
        t.forward(length/2)
        sierpinski(t, order-1, length/2)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        sierpinski(t, order-1, length/2)
        t.left(60)
        t.backward(length/2)
        t.right(60)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3
        )

t.penup()
t.goto(-200, -150)
t.pendown()

sierpinski(t, 3, 400)  # order 3
screen.mainloop()