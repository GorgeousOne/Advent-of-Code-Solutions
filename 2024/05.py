"""
https://adventofcode.com/2024/day/5
find all rows (lower input) where no y is listed before an x
given by the x|y rules (upper input)
"""

# with open("05test.txt", "r") as f:
with open("05input.txt", "r") as f:
	t = f.read().splitlines()

rs = {}
ups = []

for l in t:
	#rule
	if '|' in l:
		r1, r2 = l.split('|')
		if r1 not in rs:
			rs[r1] = []
		rs[r1].append(r2)
	#row
	elif ',' in l:
		ups.append(l.split(','))

# print("\n".join([str(x) for x in rs.items()]))
c = 0

for j, u in enumerate(ups):
	is_correct = True
	for i, x in enumerate(u):

		if x in rs and any([y in u[:i] for y in rs[x]]):
			is_correct = False
			break
	if is_correct:
		c += int(u[len(u) // 2])
print(c)