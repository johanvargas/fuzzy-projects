        # base position = 1
		# key[-1] = NUMERALS[-1]
		# key[-2] = NUMERALS[-2]
		# key[-3] = NUMERALS[-3]

		# base position = 2
		# key[-1] = NUMERALS[-3]
		# key[-2] = NUMERALS[-4]
		# key[-3] = NUMERALS[-5]

		# base position = 3
		# key[-1] = NUMERALS[-5]
		# key[-2] = NUMERALS[-6]
		# key[-3] = NUMERALS[-7]

		# base postion = 4
		# key[-1] = NUMERALS[0]
		# key[-2] = NUMERALS[-2]
		# key[-3] = NUMERALS[-3]

		# base position = 5
		# key[-1] = NUMERALS[0]
		# key[-2] = NUMERALS[-4]
		# key[-3] = NUMERALS[-5]
l = [6, 7, 9, 7]
print('{} is the actual number\n'.format(l))
l.reverse()


def convert(lst, count):

	# f'list 		= {lst}
	# count 		= {count}
	# digit 		= {lst[count]} 
	# base position = {len(str((10**count)))} 
	# base 			= {(10**count)}'

	NUMERALS = ['M', 'C', 'X', 'I']
	PENTAS = ['D', 'L', 'V']
	key = [None, None, None]
	bp = len(str((10**count)))

	def get_key(base_position, key, NUMERALS ,bp):
		# base position dictates the x1 x5 x10 it uses.
		print('get_key...')
		return NUMERALS[-(base_position)]
	
	def set_key(numeral):
		return 


	print(count,
		lst[count],
		-(len(str((10**count)))),
		(10**count),
		get_key(len(str((10**count))),
		key,
		NUMERALS ,
		bp))
	if count == (len(lst) - 1):
		return True
	print('\n')
	return convert(lst, count + 1)


check = convert(l, 0)
print(check)