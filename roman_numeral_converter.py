"""

This is my first programming project. Running a script that converts a number into its roman
numeral equivalent isn't the most challenging nor useful program, but, it is just an exercise.
As a starting point. 

When I think of projects, ones that I can forseably get done, are automation type scripts, that 
make time on the computer more efficient.

Schedule backups to external drive.

File cleanups. Check to see if there are duplicates in the specified directory.

S

"""
import timeit
import random

# Program speed.
start = timeit.default_timer()

# Essential constants & variables
SYM = ['X',  'C', 'M']
PENTA = ['V', 'L', 'D']
ONE = ['I']
ZERO = ['nulla']
key = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
zero_value = 'nulla'
sym_length = len(SYM)
penta_length = len(PENTA)


# Functions


# return array of stringified int
def get_num(num):
	x = list(str(num))
	return x


def table(lst, key):
	table = [
		key[0],
		(key[0] + key[0]),
		(key[0] + key[0] + key[0]),
		(key[0] + key[1]),
		key[1],
		(key[1] + key[0]),
		(key[1] + key[0] + key[0]),
		(key[1] + key[0] + key[0] + key[0]),
		(key[0] + key[2]),
		key[2]
	]

	def func(thing):
		return table[(int(thing) - 1)]
	return [ func(thing) for thing in lst]
"""
@@@@@@@@@@@
ADD CODE ABOVE, NOT BE DELETED. TESTING IS DONE BELOW THEM MOVED ABOVE WHEN USEFUL
GIT COMMIT AT THE END OF EACH SESSION REGARDLESS OF 
@@@@@@@@@@@

"""

def set_key(lst, count):
	if count == (len(lst) - 1):
		return ['I', 'V', 'X']
	else:
		return set_key(lst, count + 1)



# Testing functions

n = random.randint(0, 1000)

def disect(num):
	a = get_num(num)
	# b = get_base(a)
	b = table(a, set_key(a, 0))
	return [a, b]

print(disect(89))

# Program speed.

stop = timeit.default_timer()

print('Time: ', stop - start)  