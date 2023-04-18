# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
     hrs = input("Enter Hours:")
     h = float(hrs)
     rte = input("Enter Rate:")
     r = float(rte)
     if h > 40:
           above_h = h - 40
           gross_pay = 40 * r + above_h * r * 1.5
           print(gross_pay)
     else:
           gross_pay = h * r
           print(gross_pay)
except:
     print('Error, please enter numeric input')
