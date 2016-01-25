# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle
window = turtle.Screen()
window.bgcolor("white")

def draw_square():
	raphael = turtle.Turtle()
	raphael.shape("turtle")
	raphael.color("red", "green")
	raphael.speed(3)

	corners = 0
	while corners < 4:
		raphael.forward(100)
		raphael.right(90)
		corners += 1

def draw_circle():
	michelangelo = turtle.Turtle()
	michelangelo.shape("turtle")
	michelangelo.color("orange", "green")
	michelangelo.speed(3)

	michelangelo.circle(100)

def draw_triangle():
	leonardo = turtle.Turtle()
	leonardo.shape("turtle")
	leonardo.color("blue", "green")
	leonardo.speed(3)

	corners = 0
	while corners < 3:
		leonardo.right(120)
		leonardo.forward(100)
		corners += 1

def draw_star():
	donatello = turtle.Turtle()
	donatello.shape("turtle")
	donatello.color("purple", "green")
	donatello.speed(3)

	points = 0
	while points < 5:
		donatello.forward(100)
		donatello.right(144)
		donatello.forward(100)
		donatello.left(72)
		points += 1

draw_square()
draw_circle()
draw_triangle()
draw_star()
window.exitonclick()