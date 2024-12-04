"""
find all XMASs horizonontal, vertical, diagonal, forwards, backwards
"""

# with open("04test.txt", "r") as f:
with open("04input.txt", "r") as f:
	t = f.read().splitlines()

dirs = [
	(-1, -1),
	(-1, 0),
	(-1, 1),
	(0, -1),
	(0, 0),
	(0, 1),
	(1, -1),
	(1, 0),
	(1, 1)
]

num = 0
mas = "MAS"

for y, l in enumerate(t):
	for x, c in enumerate(l):
		if c != "X":
			continue
		for d in dirs:
			x2 = x
			y2 = y
			isXmas = True
			for i in range(3):
				x2 += d[0]
				y2 += d[1]
				if y2 < 0 or y2 >= len(t) or x2 < 0 or x2 >= len(l):
					isXmas = False
					break
				if t[y2][x2] != mas[i]:
					isXmas = False
					break
			if isXmas:
				num += 1

print(num)