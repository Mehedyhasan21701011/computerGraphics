import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Animated Circle")

# Create turtle
pen = turtle.Turtle()
pen.shape("circle")
pen.color("red")

# Starting position
x = -200
y = 0
pen.goto(x, y)
pen.pendown()

# Animation function
def move():
    global x
    if x < 200:
        x += 5
        pen.goto(x, y)
        screen.ontimer(move, 100)  # call move again after 50 ms

# Start animation
move()

# Keep window open
screen.mainloop()
