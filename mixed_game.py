from conversion import full_check

game_ = actual_game(quest_type)

print('Mixed Game')
rand_ = random.randrange(0,2)
print(f'random number switch {rand_}')
if rand_ == 0:				# Name
	print(f'Question -- {game_[0]}')
	ans = input('What is the answer? \n')
	check_ans(ans, game_, quest_type)
elif rand_ == 1:		# Port
	print(f'Question -- {game_[1]}')
	ans = input('What is the answer? \n')
	check_ans(ans, game_, quest_type)

def check_ans(ans, key, quest_type):
	print('Mixed Game')
	rand_ = random.randrange(0,2)
	print(f'random number switch {rand_}')
	if rand_ == 0:		# Name
		full_check(ans, key[1])
	elif rand_ == 1:		# Port
		full_check(ans, key[0])