print('shtaaht...')

# return array of stringified int
def get_num(num):
	# print('get_num running...')
	x = list(str(num))
	return x


def convert(lst, count):

	# f'list 		= {lst}
	# count 		= {count}
	# digit 		= {lst[count]} 
	# base position = {len(str((10**count)))} 
	# base 			= {(10**count)}'

	NUMERALS = ['M', 'C', 'X', 'I']
	PENTAS = ['(VM)', 'D', 'L', 'V']
	key = [None, None, None]
	bp = len(str((10**count)))

	def get_key(base_position, key, NUMERALS ,bp):
		# base position dictates the x1 x5 x10 it uses.
		# print('get_key...')
		return NUMERALS[-(base_position)]

	def set_key_test(numeral, base_pos):
		'''
		original on single.py

		Basic version to get fucntionality but not extensible beyond 10,000??
		missing function of using 'key' over later iterations on higher numbers
		plus adding high number(vinculus etc...) symbols to appropriate entries

		'''
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
		# print(key)
		return key

	print(count,
		lst[count],
		-(len(str((10**count)))),
		(10**count),
		get_key(len(str((10**count))), key, NUMERALS , bp),
		set_key_test(get_key(len(str((10**count))), key, NUMERALS, bp), len(str(10**count))),
	)
	def run_table(lst, key, count):
		print(table(lst, set_key_test(get_key(len(str((10**count))), key, NUMERALS, bp), len(str(10**count))))[count])
		return 
	run_table(lst, set_key_test(get_key(len(str((10**count))), key, NUMERALS, bp), len(str(10**count))), count)


	if count == (len(lst) - 1):
		return True
	# print('\n')
	return convert(lst, count + 1)

def table(lst, key):
	# print('table running...')
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
	return [func(thing) for thing in lst]


check = convert(get_num(89), 0)
print(check)