'''

Roman Numeral Converter v 0.02
by Johan Vargas

___WORKING NOTES_____

Working up to 1,000,000, produces string of int passed. 

BUG - Assigns multiplier (MILIMULTIPLIER) to repeats in the int.
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
	['M', 'V*', 'X*'],
	['C', 'D', 'M'],	
	['X', 'L', 'C'],
	['I' , 'V', 'X']
	)

MILLI_MULTIPLIER = ('_')

# Main Functions

# length of stringified number.
def get_int_len(num):
	return len(str(num))


# Parses number to string and returns the roman numeral unformated.
def int_to_key(num):
	int_str = str(num)
	container = ''

	for i in range(0, get_int_len(num)):
		if i + 1 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-1])
			container+=key_parser(int_str[i], MASTER_KEY[-1], int_str)
		elif i + 2 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-2])
			container+=key_parser(int_str[i], MASTER_KEY[-2], int_str)
		elif i + 3 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str)
		elif i + 4 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-4])
			container+=key_parser(int_str[i], MASTER_KEY[-4], int_str)
		elif i + 5 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-2])
			container+=key_parser(int_str[i], MASTER_KEY[-2], int_str)
		elif i + 6 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str)
		elif i + 7 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-4])
			container+=key_parser(int_str[i], MASTER_KEY[-4], int_str)
		elif i + 8 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str)

	return container

# Recieves a number and returns the roman numeral equvalent of that digit based on its position in the number.
def key_parser(digit, key, num):
	int_length = get_int_len(num)
	if digit == '0' and int_length == 1:
		return null
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
	# print('number length is ', int_length)
	# print(num.index(digit))
	if int_length > 4:		
		if num.find(digit) == 0:
			print(num, digit)
			# print(MILLI_MULTIPLIER + str(table[int(digit) - 1]))
			return MILLI_MULTIPLIER + str(table[int(digit) - 1])
		else:
			# print(table[int(digit) - 1])
			return table[int(digit) - 1]
	else:
		# print(table[int(digit) - 1])
		return table[int(digit) - 1]


# TESTING FUNCTIONS

# Test a range of numbers
def test_number_range(r):
	for n in range(0, r):
		print(int_to_key(n))

# Test a single instance, a single integer
def test_single_int(num):
	print(num, int_to_key(num))

# TESTING
test_single_int(66606)
# test_number_range(101)

	
