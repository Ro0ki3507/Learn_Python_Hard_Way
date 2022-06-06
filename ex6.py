# -*- coding: utf-8 -*-

#Store string in  variable x with a modulus operation on number 10
x = "There are %d types of people."  % 10

#Store string 'binary' on binary variable
binary = "binary"

#Store string 'don't'
do_not = "don't"

#Store string with that shows 2 variable contents (binary and do_not)
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#lines with strings: 16, 18, 19, 29 (missing line is 24)
