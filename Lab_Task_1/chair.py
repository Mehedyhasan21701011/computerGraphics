import turtle

# Screen setup
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Chair Drawing with Turtle")

# Turtle setup
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Function to draw rectangle
def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Move turtle to starting position
t.penup()
t.goto(-50, -50)  # bottom-left of the seat
t.pendown()

# Draw seat
draw_rectangle(t, 100, 20, "brown")

# Draw backrest
t.penup()
t.goto(-50, -50 + 20)
t.pendown()
draw_rectangle(t, 100, 80, "sienna")

# Draw left leg
t.penup()
t.goto(-50, -100)
t.pendown()
draw_rectangle(t, 10, 60, "gray")

# Draw right leg
t.penup()
t.goto(40, -100)
t.pendown()
draw_rectangle(t, 10, 60, "gray")

# Draw backrest supports (optional)
t.penup()
t.goto(-40, -30)
t.pendown()
draw_rectangle(t, 5, 80, "darkgray")

t.penup()
t.goto(35, -30)
t.pendown()
draw_rectangle(t, 5, 80, "darkgray")

# Hide turtle
t.hideturtle()

wn.mainloop()
