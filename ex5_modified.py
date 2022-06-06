# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
test_variable = "test"

#convert inches to cm
convert_cm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
#Adding %r as formatting
print "Test for string %r" % test_variable


#Conversion of inches  to cm
print "Conversion of height from inches to cm %d" % convert_cm

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


