#-*- coding: utf-8 -*-

from sys import argv

script, arg1, arg2 = argv

arg2 = int(arg2)

def print_arg(arg1):
	print "This is the input in argv: "
	return arg1

def calculation_sum(arg2):
	print "Doing calculation...."
	return arg2 + arg2

def formula_calc(arg3):
	print "Doing calculation from Common student question #3..."
	return arg3

x = print_arg(arg1)


print x

calc = calculation_sum(arg2 * (5 - 3))

print calc

arg3 = 24 + 34 / (1050 - 1023)

y = formula_calc(arg3)
print y




