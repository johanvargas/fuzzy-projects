import timeit

'''

feed this thing a number (int) and it will output a roman numeral equivalent.

'''
NUMERALS = ['M', 'C', 'X', 'I']
PENTAS = ['(VM)', 'D', 'L', 'V']
key = [None, None, None]
container = []
container2 = []


def get_num(num):
	# print('get_num running...')

	x = list(str(num))
	x.reverse()
	return x

def get_key(base_position, NUMERALS):
	# base position dictates the x1 x5 x10 it uses.

	# print('get_key...{} base_position {}\n'.format(NUMERALS[-(base_position)], base_position))
	return NUMERALS[-(base_position)]

def set_key_test(numeral, base_pos):
	'''
	original on single.py

	Basic version to get fucntionality but not extensible beyond 10,000??
	missing function of using 'key' over later iterations on higher numbers
	plus adding high number(vinculus etc...) symbols to appropriate entries

	'''
	# print('set_key_test...\n')
	key = [None, None, None]
	# l = lambda x : True if base_pos > 4 else False
	l = lambda x: -2 if x == 4 else -(x + 1) 
	for n in NUMERALS:
		if numeral == n:
			index = NUMERALS.index(n)
			# print(index)
			# print(NUMERALS[-(base_pos)])
			key[0] = NUMERALS[-(base_pos)]
			key[1] = PENTAS[-(base_pos)]
			key[2] = NUMERALS[l(base_pos)]
	return key

# def run_table(lst, key, count):
# 	print('run_table...')
# 	return

def table(digit, key):
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


# main function that converts 
# get_num --> array to roman numerals
# via nested functions and table()


def convert(lst, count):

	# print(lst[count])

	# f'list 		= {lst}
	# count 		= {count}
	# digit 		= {lst[count]} 
	# base position = {len(str((10**count)))} 
	# base 			= {(10**count)}'

	bp = len(str((10**count)))

	a = get_key(len(str((10**count))), NUMERALS)
	container.append(a)
	#print(a)

	b = set_key_test(a, bp)
	container.append(b)
	#print(b)

	if count == (len(lst) - 1):
		return
		

	return convert(lst, count + 1)



p = convert(get_num(53), 0)
# print(p)
# print(container)
print(get_num(53))
container.pop(0)
container.pop(1)

def hash_table(container, get_num , count):
	print(container, get_num)
	for i in get_num:
		y = table(int(i), container[get_num.index(i)])
		container2.append(y)

h = hash_table(container, get_num(53) ,0)
print(h)

print(container2)
container2.reverse()
rn = "".join(container2)
print(rn)