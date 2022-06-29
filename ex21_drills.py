#-*- coding: utf-8 -*-

from sys import argv

script, arg1 = argv

def print_arg(arg1):
	print "This is the input in argv: "
	return arg1
	
	

x = print_arg(arg1)

print x
