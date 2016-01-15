#Jan 14, 2016
#Learning Python the Hard Way Exercise 14

from sys import argv

script, user_name = argv
x = '>'

print "HI %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(x)

print "where do you live %s?" % user_name
lives = raw_input(x)

print "what kind of computer do you have?"
computer = raw_input(x)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

