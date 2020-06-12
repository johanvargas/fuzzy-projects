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
import main
# main working. Not used, just practice.
import timeit

start = timeit.default_timer()

SYM = ['I',  'X',  'C', 'M']
PENTA = ['V', 'L', 'D']

sym_length = len(SYM)

def crawl(base, digit):
	if steps <= sym_length:
		return listus[steps]
	else:
		return False

c = crawl(SYM, 4)
print(c)

stop = timeit.default_timer()

print('Time: ', stop - start)  