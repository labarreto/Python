#Jan 13, 2016
#Learning Python the Hard Way Exercise 4

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars-drivers, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

