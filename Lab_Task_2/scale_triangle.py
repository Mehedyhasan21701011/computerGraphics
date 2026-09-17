import turtle

t = turtle.Turtle()
t.speed(3)

triangle = [(0, 0), (50, 0), (25, 50)]

def draw_shape(points):
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])

# Original
draw_shape(triangle)

# Scale 2x
scaled = [(x * 2, y * 2) for x, y in triangle]
t.color("red")
draw_shape(scaled)

turtle.done()
