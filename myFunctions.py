import turtle

def draw_heart(size):
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(size / 2)
    turtle.pendown()
    turtle.left(140)
    turtle.forward(size)
    turtle.circle(size * 0.5, 200)
    turtle.right(120)
    turtle.circle(size * 0.5, 200)
    turtle.forward(size)
    turtle.setheading(0)
    turtle.end_fill()

def draw_flower(size):
    for _ in range(6):
        turtle.circle(size)
        turtle.left(60)

def fill_screen():
    turtle.colormode(255)
    turtle.speed(0)
    turtle.bgcolor(255, 220, 240)
    spacing = 120
    for y in range(-300, 301, spacing):
        for x in range(-300, 301, spacing):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            if (x + y) % 240 == 0:
                turtle.color(255, 80, 120)
                draw_heart(40)
            else:
                turtle.color(255, 150, 200)
                draw_flower(20)
