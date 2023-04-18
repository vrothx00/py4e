# Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

largest = None
smallest = None
while True:
        try:
            num = input("Enter a number: ")
            if num == "done":
                break
            num = int(num)
            if largest is None or num > largest:
                largest = num
            if smallest is None or num < smallest:
                smallest = num
        except:
            print("Invalid input")



print("Maximum is", largest)
print("Minimum is", smallest)
