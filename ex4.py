# -*- coding: utf-8 -*-

#Save car value
cars = 100

#save passengers in car
space_in_a_car = 4.0

#save how many drivers you have
drivers = 30

#save total passengers
passengers = 90

#Calculate total cars minus total drivers
cars_not_driven = cars - drivers


cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
