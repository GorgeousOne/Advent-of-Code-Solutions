# https://adventofcode.com/2023/day/4

import re
import numpy as np

# with open("day04_input copy.txt") as file:
with open("day04_input.txt") as file:
	text = file.read().splitlines()

card_scores = {}
num_cards = {}

for i, line in enumerate(text):
	nums = line.split(":")[1]
	win_text, num_text = nums.split("|")

	win_nums = [int(s) for s in re.findall(r"\d+", win_text)]
	nums = [int(s) for s in  re.findall(r"\d+", num_text)]

	correct_nums = 0
	for num in nums:
		if num in win_nums:
			correct_nums += 1
	card_scores[i + 1] = correct_nums
	num_cards[i + 1] = 1

for i in range(1, len(card_scores) + 1):
	card_num = num_cards[i]

	for j in range(1, card_scores[i] + 1):
		num_cards[i + j] += card_num

# print(num_cards)
print(sum(num_cards.values()))

