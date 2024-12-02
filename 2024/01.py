
# with open("01test.txt", "r") as f:
with open("01input.txt", "r") as f:
	text = f.read().splitlines()

l1 = []
l2 = []
for line in text:
	c = line.split()
	l1.append(int(c[0]))
	l2.append(int(c[1]))

diffs = 0
while len(l1) > 0:
	min1 = min(l1)
	min2 = min(l2)
	l1.remove(min1)
	l2.remove(min2)
	print(min1, min2, "=>", min2 - min1)
	diffs += abs(min2 - min1)

print(diffs)
