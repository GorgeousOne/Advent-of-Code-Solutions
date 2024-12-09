import os.path
import sys

template_code = '''"""
https://adventofcode.com/2024/day/{d}

"""
import re
import numpy as np
from collections import defaultdict

with open("{day}test.txt", "r") as f:
#with open("{day}input.txt", "r") as f:
	t = f.read().splitlines()

# for y, l in enumerate(t):
# 	for x, c in enumerate(l):
# for l in t:
'''

def setup_day(i):
	day_name = str(i).zfill(2)
	if not os.path.isfile(day_name + '.py'):
		with open(day_name + '.py', 'w') as f:
			f.write(template_code.format(d=i, day=day_name))
	# if not os.path.isfile(day_name + 'input.txt'):
	# 	open(day_name + 'input.txt', 'a', encoding='utf-8').close()
	if not os.path.isfile(day_name + 'test.txt'):
		open(day_name + 'test.txt', 'a', encoding='utf-8').close()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		import datetime
		day = datetime.datetime.now().day
	else:
		day = sys.argv[1]

	try:
		day = int(day)
	except ValueError:
		print('Day must be an integer')
		sys.exit(1)
	if day < 1 or day > 25:
		print('Day must be between 1 and 25')
		sys.exit(1)

	setup_day(day)