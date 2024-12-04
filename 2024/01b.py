"""
sum all (x from list1) * (occurences x in list2)
"""

# with open("01test.txt", "r") as f:
with open("01input.txt", "r") as f:
	text = f.read().splitlines()

l1 = []
l2 = []
for line in text:
	c = line.split()
	l1.append(int(c[0]))
	l2.append(int(c[1]))

sims = 0
for x in l1:
	sims += x * l2.count(x)

print(sims)
