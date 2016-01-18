#Jan 17, 2016
#Learning Python the Hard Way Exercise 21

def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "Subtrating %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b

age = add(15, 5)
height = subtract(67, 4)
weight = multiply (60, 2)

print "Age: %d, Height: %d, Weight: %d" % (age, height, weight)
