import turtle
window = turtle.Screen()
window.bgcolor("white")

alpha = turtle.Turtle()
alpha.shape(None)
alpha.color("blue")
alpha.speed(10)

def draw_square(turtle):
	turtle.fill(True)
	for i in range(1,5):
		turtle.forward(10)
		turtle.right(90)
	turtle.fill(False)

def draw_fractal(turtle):
	for i in range(1,5):
		for i in range(1,3):
			draw_square(turtle)
			turtle.forward(10)
		turtle.forward(10)
		turtle.right(90)

def draw_sierpinski(turtle):
	for i in range(1,2):
		draw_fractal(turtle)
		turtle.right(90)
		turtle.forward(30)
	turtle.hideturtle()

#draw_square(alpha)
draw_fractal(alpha)
#draw_sierpinski(alpha)
window.exitonclick()