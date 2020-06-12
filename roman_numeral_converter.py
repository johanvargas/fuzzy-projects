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

# Program speed.
start = timeit.default_timer()

# Essential constants & variables
SYM = ['I',  'X',  'C', 'M']
PENTA = ['V', 'L', 'D']

sym_length = len(SYM)
penta_length = len(PENTA)



# Functions

# return array of stringified int
def get_num(num):
	x = list(str(num))
	return x

"""
@@@@@@@@@@@
ADD CODE ABOVE, NOT BE DELETED. TESTING IS DONE BELOW THEM MOVED ABOVE WHEN USEFUL
GIT COMMIT AT THE END OF EACH SESSION REGARDLESS OF 
@@@@@@@@@@@

"""

def check_base(ary, digit):
	l = len(ary)
	#print(f'{l+1} is the length of the arrayed integer.')
	return (10**l)


# Testing functions

def test1():
	for n in range(0, 10000, 100):
		print(f'\n{n}')
		print(check_base(get_num(n)))
print(test1())

# Program speed.

stop = timeit.default_timer()

print('Time: ', stop - start)  