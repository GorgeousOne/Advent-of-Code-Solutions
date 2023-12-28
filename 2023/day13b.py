# https://adventofcode.com/2023/day/13

# with open("day13_input copy.txt") as file:
with open("day13_input.txt") as file:
	text = file.read().splitlines()

pattern_rows = []
pattern_cols = []
rows = []

for i, line in enumerate(text):
	if line == "":
		# print("space", i)
		cols = ["".join([rows[row][col] for row in range(len(rows))]) for col in range(len(rows[0]))]
		pattern_rows.append(rows)
		pattern_cols.append(cols)
		rows = []
		continue
	rows.append(line)

def diffs(s1, s2):
	diffs = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			diffs += 1
	return diffs

def get_mirror_i(pattern):
	mirror_i = -1
	size = len(pattern)

	for start in range(size - 1):
		max_delta = min(start + 1, size - 1 - start)
		is_mirror = True
		has_smudge = False

		for delta in range(max_delta):
			diff = diffs(pattern[start - delta], pattern[start + 1 + delta])
			if diff > 1 or (diff == 1 and has_smudge):
				is_mirror = False
				break
			if diff == 1:
				has_smudge = True

		if is_mirror and has_smudge:
			mirror_i = start
			break

	return mirror_i

sums = 0

for i in range(len(pattern_cols)):

	rows = pattern_rows[i]
	cols = pattern_cols[i]
	mirror_y = get_mirror_i(rows)

	if mirror_y != -1:
		sums += 100 * (mirror_y + 1)
		continue

	mirror_x = get_mirror_i(cols)
	if mirror_x != -1:
		sums += mirror_x + 1
	else:
		print("meh", i)

print(sums)

