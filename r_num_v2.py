'''

Integer to Roman Numeral version 0.02
by Johan Vargas
10292020

###############################################################

WORKING NOTES

Working up to 1,000,000, produces string from int passed. 

int_to_key needs to be handled batter, iterator or something.

###############################################################

REFERENCES

I = 1

V = 5

X = 10

L = 50

C = 100

D = 500

M = 1000

_V = 5000

_, is the line over the Numeral that equal Numeral X 1000 = _Numeral

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


# Parses number to string and returns the roman numeral as string.
def int_to_key(num):
	int_str = str(num)
	container = ''

	for i in range(0, get_int_len(num)):
		if i + 1 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-1])
			container+=key_parser(int_str[i], MASTER_KEY[-1], int_str, i)
		elif i + 2 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-2])
			container+=key_parser(int_str[i], MASTER_KEY[-2], int_str, i)
		elif i + 3 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str, i)
		elif i + 4 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-4])
			container+=key_parser(int_str[i], MASTER_KEY[-4], int_str, i)
		elif i + 5 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-2])
			container+=key_parser(int_str[i], MASTER_KEY[-2], int_str, i)
		elif i + 6 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str, i)
		elif i + 7 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-4])
			container+=key_parser(int_str[i], MASTER_KEY[-4], int_str, i)
		elif i + 8 == len(int_str):
			# print(int_str[i], i, num, MASTER_KEY[-3])
			container+=key_parser(int_str[i], MASTER_KEY[-3], int_str, i)

	return container

# Receives a number and returns the roman numeral equvalent of that digit based on its position in the number.
def key_parser(digit, key, num, i):
	int_length = get_int_len(num)
	if digit == '0' and int_length == 1:
		return null
	if digit == '0':
		return ''
	# Table is the key for decimal roman numeral pattern
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
		if i == 0:
			# print(num, digit, num.find(digit))
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
    # r - the range from, 0 to r to print
	for n in range(0, r):
		print(int_to_key(n))

# Test a single instance, a single integer
def test_single_int(num):
	print(num, int_to_key(num))

# TESTING
single_int = 88
t_range = 20

print(single_int)
test_single_int(single_int)

print(t_range)
test_number_range(t_range)
