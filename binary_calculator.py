def addition(x,y):
	answer = bin(x + y)
	return answer

def subtraction(x,y):
	answer = bin(x - y)
	return answer

def multiplication(x,y):
	answer = bin(x * y)
	return answer

def division(x,y):
	answer = bin(x / y)
	return answer

def calculator():
	x = int(raw_input("What is the first number? "))
	y = int(raw_input("What is the second number? "))
	menu = raw_input("Do you want to add, subtract, multiply, or divide? ")
	if menu == "add":
		print addition(x,y)
	if menu == "subtract":
		print subtraction(x,y)
	if menu == "multiply":
		print multiplication(x,y)
	if menu == "divide":
		print division(x,y)

calculator()