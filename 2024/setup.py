import os.path

template_code = '''
import re
import numpy as np

with open("{day}test.txt", "r") as f:
#with open("{day}input.txt", "r") as f:
	t = f.read().splitlines()

#l1 = [int(l) for l in t]
#for x in l1:

#l1 = []
#for l in t:
#	c = l.split()
#	l1.append()
'''

for i in range(1, 26):
	day_name = str(i).zfill(2)
	if not os.path.isfile(day_name + '.py'):
		with open(day_name + '.py', 'w') as f:
			f.write(template_code.format(day=day_name))
	# if not os.path.isfile(day_name + 'input.txt'):
	# 	open(day_name + 'input.txt', 'a', encoding='utf-8').close()
	if not os.path.isfile(day_name + 'test.txt'):
		open(day_name + 'test.txt', 'a', encoding='utf-8').close()