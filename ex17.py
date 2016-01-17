#Jan 16, 2016
#Learning Python the Hard Way Exercise 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read() 
# open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
# open(to_file, 'w').write(indata)
print "Alright, all done."

out_file.close()
in_file.close()

# entire file can be replaced with
# open(to_file, 'w').write(open(from_file).read())