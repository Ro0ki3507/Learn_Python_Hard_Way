# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to read file content from %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: \n")
line2 = raw_input("line 2: \n")
line3 = raw_input("line 3: \n")

print "I'm going to write these to the file."
print "%s \n%s \n%s" % (line1,line2,line3)
lines = [line1,"\n",line2,"\n",line3]

target.writelines(lines)
print "Closing file...."
target.close()


#Read file content and print
print "\n"
print "Now printing file content"
target = open(filename)
print target.read()

print "And finally, we close it again."
target.close()

