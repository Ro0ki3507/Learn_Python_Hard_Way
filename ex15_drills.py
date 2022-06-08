# -*- coding: utf-8 -*-

#Import feature argv from module sys
from sys import argv

#Set variables as arguments
script, filename = argv

#Open file name input in filename variable
txt = open(filename)

#Print filename and content
print "Here's your file %r:" % filename
print txt.read()
txt.close()

#Get input of filename again
print "Type the filename again:"
file_again = raw_input("> ")

#Open file again
txt_again = open(file_again)

#Print file content
print txt_again.read()
txt_again.close()
