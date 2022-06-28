#-*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

#function to print all document
def print_all(f):
	print f.read()
	
#function to set cursor at initial part of file
def rewind(f):
	f.seek(0)

#function to print each line
def print_a_line(line_count,f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

