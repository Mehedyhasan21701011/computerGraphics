import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Rectangle with Turtle")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.color("green")

# Draw rectangle
width = 150
height = 80

for _ in range(2):
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)

# Hide turtle
pen.hideturtle()

# Keep window open
screen.mainloop()