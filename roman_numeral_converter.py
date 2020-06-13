"""

This is my first programming project. Running a script that converts a number into its roman
numeral equivalent isn't the most challenging nor useful program, but, it is just an exercise.
As a starting point. 

When I think of projects, ones that I can forseably get done, are automation type scripts, that 
make time on the computer more efficient.

Schedule backups to external drive.

File cleanups. Check to see if there are duplicates in the specified directory.

Use Generators in update. and maybe lambda functions??
list conprehension

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
	print('get_num running...')
	x = list(str(num))
	return x


def table(lst, key):
	print('table running...')
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
# def convert(lst, count):

# 	# f'list 		= {lst}
# 	# count 		= {count}
# 	# digit 		= {lst[count]} 
# 	# base position = {len(str((10**count)))} 
# 	# base 			= {(10**count)}'

# 	NUMERALS = ['M', 'C', 'X', 'I']
# 	PENTAS = ['(VM)', 'D', 'L', 'V']
# 	key = [None, None, None]
# 	bp = len(str((10**count)))

# 	def get_key(base_position, key, NUMERALS ,bp):
# 		# base position dictates the x1 x5 x10 it uses.
# 		print('get_key...')
# 		return NUMERALS[-(base_position)]

# 	def set_key_test(numeral, base_pos):
# 		'''
# 		original on single.py

# 		Basic version to get fucntionality but not extensible beyond 10,000??
# 		missing function of using 'key' over later iterations on higher numbers
# 		plus adding high number(vinculus etc...) symbols to appropriate entries

# 		'''
# 		key = [None, None, None]
# 		# l = lambda x : True if base_pos > 4 else False
# 		l = lambda x: -2 if x == 4 else -(x + 1) 
# 		for n in NUMERALS:
# 			if numeral == n:
# 				index = NUMERALS.index(n)
# 				print(index)
# 				print(NUMERALS[-(base_pos)])
# 				key[0] = NUMERALS[-(base_pos)]
# 				key[1] = PENTAS[-(base_pos)]
# 				key[2] = NUMERALS[l(base_pos)]
# 		print(key)
# 		return key

# 	print(count,
# 		lst[count],
# 		-(len(str((10**count)))),
# 		(10**count),
# 		get_key(len(str((10**count))), key, NUMERALS , bp),
# 		set_key_test(get_key(len(str((10**count))), key, NUMERALS, bp), len(str(10**count)))
# 	)
# 	if count == (len(lst) - 1):
# 		return True
# 	print('\n')
# 	return convert(lst, count + 1)

def set_key(lst, count):
	print('set_key running...')
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