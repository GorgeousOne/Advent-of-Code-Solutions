"""
https://adventofcode.com/2024/day/4
find all
M S
 A
M S
shapes (forwards, backwards)
"""

# with open("04test.txt", "r") as f:
with open("04input.txt", "r") as f:
	t = f.read().splitlines()

num = 0

for y, l in enumerate(t):
	for x, c in enumerate(l):
		if c != "A":
			continue
		if x < 1 or x >= len(l)-1 or y < 1 or y >= len(t)-1:
			continue
		d1 = [t[y-1][x-1], t[y+1][x+1]]
		d2 = [t[y-1][x+1], t[y+1][x-1]]

		if "M" in d1 and "S" in d1 and "M" in d2 and "S" in d2:
			num += 1
print(num)