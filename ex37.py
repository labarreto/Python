#Feb 26th

#there's no specific exercise but I'm going to test out a few terms
#i don't know in the list given. 



# @ --> decorator 

add = wrapper(add)

def add(a, b):
	return Coordinate(a.x + b.x, a.y + b.y)

# ^ ^ ^ that is the same as:

@wrapper
def add(a,b):
	return Coordinate(a.x + b.x, a.y + b.y)

# difference between Java and Python in data types:
# Jave has floats, doubles, long, int, Big Integer, etc. 
# Python only has numbers for storing 
#  integers, and floats for storing decimals