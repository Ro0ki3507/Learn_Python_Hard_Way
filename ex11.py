# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)



#Examples to see difference between input() and raw_input()

print "Enter value1= "
value1 = input()
total = value1 * 10

print "Enter value2= "
value2 = raw_input()
total2 = value2 * 10

print total
print total2

