# Exercise 2: Write a program that uses input to prompt a user for their
# name and then welcomes them.
# Enter your name: Chuck
# Hello Chuck
name = input("Enter your name: ")
print(f"Hello {name}")

# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
hrs = input("Enter Hours:")
rte = input("Enter Rate:")
hrs = int(hrs)
rte = float(rte)
gross_pay = rte * hrs
print(f"Pay: {gross_pay}")

# We won’t worry about making sure our pay has exactly two digits after the decimal
# place for now. If you want, you can play with the built-in Python round function
# to properly round the resulting pay to two decimal places.
# Exercise 4: Assume that we execute the following assignment statements:

width = 17
height = 12.0

# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).

print(type(width//2))
print(type(width/2.0))
print(type(height/3))
print(type(1 + 2 * 5))

# Use the Python interpreter to check your answers.
# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
# converted temperature.
celsius = int(input("Enter a celsius temp "))
fahr = (celsius * 1.8) + 32
print(f"Fahrenheit {fahr}")
