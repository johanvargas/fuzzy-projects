'''
___WORKING NOTES
Working up to 9999, unformated, ugly. 10292020
________

I = 1

V = 5

X = 10

L = 50

C = 100

D = 500

M = 1000

_V = 5000

_, is the line over the Numeral that equal Numeral X 1000 = _Numeral

numeral_key = {0: 'nulla', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

UNI = ['I' , 'V'  'X']

DECI = ['X', 'L', 'C']

CENTI = ['C', 'D', 'M']

MILLI = ['M', '_V', '_X']

#############################################################################

nulla

I V X

X L C

C D M

M _V _X

_X _V _L

_C _D _M 

... and so on

##############################################################################

get_int_len -> get_key

'''

# KEYS 

null = 'nulla'

MASTER_KEY = (
	['M', '_V', '_X'], 
	['C', 'D', 'M'], 
	['X', 'L', 'C'], 
	['I' , 'V', 'X']
	)

MILLI_MULTIPLIER = '_'

# Main Functions

def get_int_len(num):
	return len(str(num))

def int_to_key(num):
	int_str = str(num)
	container = ''

	for i in range(0, get_int_len(num)):
		if i + 1 == len(int_str):
			print(int_str[i], i, num, MASTER_KEY[-1])
			key_parser(int_str[i], MASTER_KEY[-1])
		elif i + 2 == len(int_str):
			print(int_str[i], i, num, MASTER_KEY[-2])
			key_parser(int_str[i], MASTER_KEY[-2])
		elif i + 3 == len(int_str):
			print(int_str[i], i, num, MASTER_KEY[-3])
			key_parser(int_str[i], MASTER_KEY[-3])
		elif i + 4 == len(int_str):
			print(int_str[i], i, num, MASTER_KEY[-4])
			key_parser(int_str[i], MASTER_KEY[-4])

	return container

def key_parser(digit, key):
	if digit == '0':
		return ''
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
	print(table[int(digit) - 1])
	return table[int(digit) - 1]


# TESTING FUNCTIONS

# Test a range of numbers
def test_number_range(r):
	for n in range(0, r):
		print(int_to_key(n))

# Test a single instance, a single integer
def test_single_int(num):
	print(int_to_key(num))

# TESTING
test_single_int(69)
