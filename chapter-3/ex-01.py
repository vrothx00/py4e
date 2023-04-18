# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

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
