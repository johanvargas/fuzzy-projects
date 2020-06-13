l = [6, 7, 4]

print('{} is the actual number'.format(l))


def convert(lst, count):

	# print(
	# f'list = {lst} : count = {count} : digit = {lst[count]} : 
	# base-position = {len(str((10**count)))} : base = {(10**count)}'
	# )

	NUMERALS = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	key = [None, None, None]

	def get_key(base_position, key, NUMERALS):
		internal_count = 0
		# base position dictates the x1 x5 x10 it uses.

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
		print(base_position, NUMERALS[-(base_position)], NUMERALS[-(base_position + 2)], NUMERALS[-(base_position + 3)])
		key

		return key
	print(
		lst,											# listed integers reversed()
		count,											# current index of list
		lst[count],										# digit
		len(str((10**count))),							# base position - length of base
		(10**count),									# base
		get_key(len(str((10**count))), key, NUMERALS) 	# 
		)
	if count == (len(lst) - 1):
		return True
	print('\n')
	return convert(lst, count + 1)


check = convert(l, 0)
print(check)