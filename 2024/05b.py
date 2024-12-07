"""
https://adventofcode.com/2024/day/5
sort all rows (lower input) where an y is listed before an x
given by the 'x|y' rules (upper input) so that each row
satisfies all rules
"""
from collections import defaultdict

# with open("05test.txt", "r") as f:
with open("05input.txt", "r") as f:
	t = f.read().splitlines()

rs = defaultdict(list)
ups = []
for l in t:
	if '|' in l:
		r1, r2 = l.split('|')
		rs[r1].append(r2)
	elif ',' in l:
		ups.append(l.split(','))

# print("\n".join([str(x) for x in rs.items()]))

def is_c(u, rs):
	for i, x in enumerate(u):
		if x in rs and any([y in u[:i] for y in rs[x]]):
			return False
	return True

c = 0
cs = []
for j, u in enumerate(ups):
	if is_c(u, rs):
		continue
	while not is_c(u, rs):
		for k, x in enumerate(u):
			if x not in rs:
				continue
			for y in rs[x]:
				if y in u[:k]:
					u.remove(x)
					u.insert(u.index(y), x)
					break
	c += int(u[len(u) // 2])
print(c)