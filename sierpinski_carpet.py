import turtle
window = turtle.Screen()
window.bgcolor("white")

alpha = turtle.Turtle()
alpha.shape(None)
alpha.color("blue")
alpha.speed(0)
alpha.penup()
alpha.goto(-200,200)
alpha.pendown()

def draw_square(turtle, size):
	turtle.fill(True)
	for i in range(1,5):
		turtle.forward(size)
		turtle.right(90)
	turtle.fill(False)

def draw_fractal(turtle, size):
	"""Draws a larger square with the middle square missing."""
	for i in range(1,5):
		for i in range(1,3):
			draw_square(turtle, size)
			turtle.forward(size)
		turtle.forward(size)
		turtle.right(90)

def draw_fractal2(turtle, size):
	for i in range(1,5):
		for i in range(1,3):
			draw_fractal(turtle, size)
			turtle.forward(size * 3)
		turtle.forward(size * 3)
		turtle.right(90)

def draw_fractal3(turtle, size):
	for i in range(1,5):
		for i in range(1,3):
			draw_fractal2(turtle, size)
			turtle.forward(size * 9)
		turtle.forward(size * 9)
		turtle.right(90)

def draw_fractal4(turtle, size):
	for i in range(1,5):
		for i in range(1,3):
			draw_fractal3(turtle, size)
			turtle.forward(size * 27)
		turtle.forward(size * 27)
		turtle.right(90)

draw_square(alpha, 2)
#draw_fractal(alpha, 2)
#draw_fractal2(alpha, 1)
#draw_fractal3(alpha, 2)
#draw_fractal4(alpha, 2)

alpha.hideturtle()
window.exitonclick()