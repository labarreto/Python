#Jan 16, 2016
#Learning Python the Hard Way Exercise 18


def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print2(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print1(arg1):
	print "arg1: %r" % arg1

def printNone():
	print "I got nothin'."

print_two("Great", "Panda")
print2("Panda", "Bear")
print1("one")
printNone()