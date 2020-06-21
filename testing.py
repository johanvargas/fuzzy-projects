from pop import convert, get_num, table
import random

r = random.randint(0, 1000)
print('{} is out number\n'.format(r))
check = convert(get_num(r), 0)
print(check)
