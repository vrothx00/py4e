# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(h, r):
    if h > 40:
        over_pay = h - 40
        gross_pay = 40 * r + over_pay * r * 1.5
    else:
        gross_pay = h * r
    return gross_pay

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
p = computepay(h, r)
print("Pay", p)
