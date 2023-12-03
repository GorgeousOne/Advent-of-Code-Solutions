import os

aoc_directory = "./2023"

for day in range(1, 26):
	python_file = os.path.join(aoc_directory, f"day{day:02}.py")
	text_file = os.path.join(aoc_directory, f"day{day:02}_input.txt")

	if not os.path.exists(python_file):
		with open(python_file, "w") as file:
			file.write(f"""# Day {day}

import re
import numpy as np

#with open("day{day:02}_input copy.txt") as file:
with open("day{day:02}_input.txt") as file:
	text = file.read().splitlines()

for line in text:
	""")

	if not os.path.exists(text_file):
		with open(text_file, "w") as file:
			pass
