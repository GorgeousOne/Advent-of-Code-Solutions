# Day 1
import re
import copy

# with open("day01_input copy.txt") as file:
with open("day91_input.txt") as file:
	text = file.read().splitlines()

# sums = 0
# for line in text:
# 	matches = "".join(re.findall(r"\d+", line))
# 	sums += int(matches[0] + matches[-1])
# print(sums)

word_nums = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"four" : 4,
	"five" : 5,
	"six" : 6,
	"seven" : 7,
	"eight" : 8,
	"nine" : 9,
}

text2 = copy.deepcopy(text)

for i, line in enumerate(text2):

	indices = {}
	line2 = line
	for key, val in word_nums.items():
		for onematch in re.finditer(key, line):
			idx = onematch.start()
			line2 = line2[:idx] + str(val) + line2[idx + 1:]
	text2[i] = line2
	

sums2 = 0
for i, line in enumerate(text2):
	matches = "".join(re.findall(r"\d+", line))
	sums2 += int(matches[0] + matches[-1])

print(sums2)