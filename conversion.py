def full_check(ans, key):
	print(f'full_check... answer : {ans} -- key {key}')
	inner_ans = str(ans)
	inner_key = str(key)

	if inner_ans == inner_key:
		print('correct')
	else:
		print('incorrect')
