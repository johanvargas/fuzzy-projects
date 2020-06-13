import random
l = [6, 7, 4]
def convert(lst, count):
	# print(
	# f'list = {lst} : count = {count} : digit = {lst[count]} : 
	# base-position = {len(str((10**count)))} : base = {(10**count)}'
	# )

	NUMERALS = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	key = [None, None, None]

	def get_key(base_position):
		# base position dictates the x1 x5 x10 it uses.

		# key[-1] = NUMERALS[-1]
		# key[-2] = NUMERALS[-2]
		# key[-3] = NUMERALS[-3]

		# key[-1] = NUMERALS[-3]
		# key[-2] = NUMERALS[-4]
		# key[-3] = NUMERALS[-5]

		# key[-1] = NUMERALS[-5]
		# key[-2] = NUMERALS[-6]
		# key[-3] = NUMERALS[-7]

		# key[-1] = NUMERALS[0]
		# key[-2] = NUMERALS[-2]
		# key[-3] = NUMERALS[-3]

		key[-1] = NUMERALS[0]
		key[-2] = NUMERALS[-4]
		key[-3] = NUMERALS[-5]
		return key
	print(lst, count, lst[count], len(str((10**count))), (10**count), get_key(len(str((10**count)))))
	lst.reverse()
	print(lst)
	if count == (len(lst) - 1):
		return True

	return convert(lst, count + 1)


check = convert(l, 0)
print(check)