NUMERALS = ['M', 'C', 'X', 'I']
PENTAS = ['5000/filler','D', 'L', 'V']

def set_key_test(numeral):
	# Basic version to get fucntionality but not extensible beyond 10,000??
	# missing function of using 'key' over later iterations on higher numbers
	# plus adding high number(vinculus etc...) symbols to appropriate entries
	key = [None, None, None]
	for n in NUMERALS:
		if numeral == n:
			key[0] = n
			key[1] = PENTAS[NUMERALS.index(n)]
			key[2] = NUMERALS[NUMERALS.index(n) - 1]
	#print(key)
	return key

a = set_key_test('I')
b = set_key_test('X')
c = set_key_test('C')
d = set_key_test('M')

print(a)
print(b)
print(c)
print(d)