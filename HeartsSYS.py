import turtle
from math import pi, sin, cos

def draw_heart(w, h, color, start_pos):
    t.pensize(2.5)
    t.up()
    t.goto(start_pos)
    t.down()
    t.fillcolor(color)
    t.begin_fill()

    a = 0
    points = []
    while a < 2 * pi:
        x = w * (16 * sin(a) ** 3) + start_pos[0]
        y = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a)) + start_pos[1]
        points.append((x, y))
        if len(points) == 1:
            t.up()
            t.goto(points[0])  # Move to the starting point
            t.down()
        else:
            t.goto(x, y)
        a += 0.01 
    t.goto(points[0])  # Close the shape
    t.end_fill()

def draw_text(text, position):
    t.up()
    t.goto(position)
    t.color("black")
    t.write(text, align="center", font=("Verdana", 15, "bold"))
    t.down()

# Define vibrant and cheerful colors
colors = ['#FF1493', '#FF6347', '#00BFFF', '#FFFF00', '#FFA500']

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("See You Soon..")

# Create a turtle instance
t = turtle.Turtle()
t.hideturtle()

# Draw three hearts with different initial sizes and colors
for i, color in enumerate(colors):
    size = 16 - i * 2
    draw_heart(size, size, color, (0, 0))

# Draw farewell message
draw_text("See You Soon.. <3", (0, -30))

# Keep the window open
turtle.done()
