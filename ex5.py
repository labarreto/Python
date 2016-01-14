#Jan 13, 2016
#Learning Python the Hard Way Exercise 5

name = 'Laura Barreto'
age = 20
height = 62 #inches
weight = 120 #lbs
eyes = 'Brown'
hair = 'Dark Brown'
# %d - format a number for display
# %s - insert the presentation string
# %r - insert canonical string


print "Let's talk about %s." % name
print "She's %s inches tall." % height
print "She's %s pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair" % (eyes, hair)

print "If I add %d, %d, and %d, I get %d." % (
	age, height, weight, age + height + weight)