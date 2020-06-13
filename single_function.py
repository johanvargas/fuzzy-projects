NUMERALS = ['M', 'C', 'X', 'I']
# PENTAS = ['5000/filler','D', 'L', 'V']

# def set_key_test(numeral):
# 	# Basic version to get fucntionality but not extensible beyond 10,000??
# 	# missing function of using 'key' over later iterations on higher numbers
# 	# plus adding high number(vinculus etc...) symbols to appropriate entries
# 	key = [None, None, None]
# 	for n in NUMERALS:
# 		if numeral == n:
# 			key[0] = n
# 			key[1] = PENTAS[NUMERALS.index(n)]
# 			key[2] = NUMERALS[NUMERALS.index(n) - 1]
# 	#print(key)
# 	return key

# a = set_key_test('I')
# b = set_key_test('X')
# c = set_key_test('C')
# d = set_key_test('M')

# print(a)
# print(b)
# print(c)
# print(d)

seperator = ','

print(seperator.join(NUMERALS))

s = 3/3

print(s)


'''
scraps, should be thrown out when functional

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
'''