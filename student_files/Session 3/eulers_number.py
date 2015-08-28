# This program is designed to estimate the mathematical constant "e" (aka Euler's number)
# "e" is a common quantity across mathematics and is of great importance to many scientific fields
# We define "e" as the limit of (1+1/n)^n as n approaches infinity
# "e" is approximately equal to 2.71828

# the following method approximates "n" to a given decimal place
def approximate(digits):
	# set n
	n = 1
	#loop will run indefinitely until approximation is reached
	while True:
		# approximate by plugging n into (1+1/n)^n
		e = float((1 + 1.0/n)**n)
		if (decimal_places(e) >= digits):
			return ("approximation of e to {0} digits = {1}".format(digits, round(e, digits)))
		print(e)
		n += 1


# there is a little bit of cheekiness going on here this method calculates the number of digits 
# following the decimal by turning the number into a string, splitting the string at the decimal
# and finding the length of the second element 
def decimal_places(num):
	return len(str(num).split(".")[1])

if __name__ == '__main__':
	# loop to ask the user for input indefinitely (until given exit signal, ctrl+c)
	while True:
		digits = input("approximate 'e' to how how many decimal places?: ")
		print(approximate(digits))




