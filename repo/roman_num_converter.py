import timeit
import random

'''
NOT WORKING PROPERLY --> r_num_v2 WORKING
feed this thing a number (int) and it will output a roman numeral equivalent.
####################

I = 1

V = 5

X = 10

L = 50

C = 100

D = 500

M = 1000

_V = 5000

_, is the line over the Numeral that equal Numeral X 1000 = _Numeral

####################

get_num, changes the int to a reverse list of that int

get_key, gets

'''

NUMERALS = ['M', 'C', 'X', 'I']
PENTAS = ['D', 'L', 'V']
key = [None, None, None]
container = []
container2 = []

def get_num(num):
	# CONVERTS AN INT TO A STRING LIST OF THAT INT, THEN REVERSE.
	x = list(str(num))
	x.reverse()
	return x

def get_key(base_position, NUMERALS):
	# CALLED BY convert first.
	# base position dictates the x1 x5 x10 it uses.
	print('get_key...{} base_position {}\n'.format(NUMERALS[-(base_position)], base_position))
	return NUMERALS[-(base_position)]

def set_key_test(numeral, base_pos):
	# print('set_key_test...\n')
	key = [None, None, None]
	l = lambda x: -2 if x == 4 else -(x + 1) 
	for n in NUMERALS:
		if numeral == n:
			# index = NUMERALS.index(n)
			# print(index)
			# print(NUMERALS[-(base_pos)])
			key[0] = NUMERALS[-(base_pos)]
			key[1] = PENTAS[-(base_pos)]
			key[2] = NUMERALS[l(base_pos)]
	return key

def table(digit, key):
	if digit == 0:
		return 'nulla'
	# print('table...')
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
	return table[int(digit) - 1]

def convert(lst, count):
	# MAIN FUNCTION 
	# print(lst[count])
	# f'list 		= {lst}
	# count 		= {count}
	# digit 		= {lst[count]} 
	# base position = {len(str((10**count)))} 
	# base 			= {(10**count)}'

	bp = len(str((count)))
	# print(bp)

	a = get_key(len(str((count))), NUMERALS)
	container.append(a)
	# print(a)

	b = set_key_test(a, bp)
	container.append(b)
	# print(b)

	if count == (len(lst) - 1):
		return
		
	return convert(lst, count + 1)


# HELPER FUNCTIONS TO PARSE THE LISTS THAT CONTAIN THE CONVERSION FROM INT TO ROMAN NUMERAL

def clean_container(container):
	for i in container:
		if len(i) == 1:
			container.remove(i)
	return container

def print_num(clean_container, get_num):
	for t in range(len(get_num)):
		# print(table(get_num[t], clean_container[int(t)]))
		container2.append(table(get_num[t], clean_container[int(t)]))

# r = random.randint(0, 10000)

# TEST FUNCTIONS
def test(r):

	g = get_num(r)
	p = convert(g, 0)
	g.reverse()
	clean = clean_container(container)
	p = print_num(clean, g)
	container2.reverse()
	j = ''.join(container2)
	print(r, j)

for n in range (0, 11):
	test(n)
	container = []
	container2 = []

test(69)
