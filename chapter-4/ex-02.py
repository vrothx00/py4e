# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score

score = input("Enter Score: ")


def computegrade(s):
	try:
		s = float(score)
		if s > 1 or s < 0:
			print('You entered a value out of range')
		elif s >= 0.9:
			print('A')
		elif s >= 0.8:
			print('B')
		elif s >= 0.7:
			print('C')
		elif s >= 0.6:
			print('D')
		elif s < 0.6:
			print('F')
	except:
		print("Bad score")


computegrade(score)
