
# with open("02test.txt", "r") as f:
with open("02input.txt", "r") as f:
	t = f.read().splitlines()

rows = [[int(x) for x in l.split()] for l in t]
safes = 0

def is_safe(row):
	if row[0] > row[1]:
		row = row[::-1]
	for i in range(len(row) - 1):
		d = row[i+1] - row[i]
		if d < 1 or d > 3:
			return 0
	return 1


for row in rows:
	row_safe = 0
	row_safe += is_safe(row)
	for j in range(len(row)):
		c = row[:]
		del c[j]
		row_safe += is_safe(c)
	safes += 1 if row_safe > 0 else 0

print(safes)