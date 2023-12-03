# Day 2

config = {
	"red": 12,
	"green": 13,
	"blue": 14 
}

# with open("day02_input copy.txt") as file:
with open("day02_input.txt") as file:
	text = file.read().splitlines()

games = []

for line in text:
	grabs = []
	line = " ".join(line.split()[2:])
	grab_texts = line.split(";")

	for grab_text in grab_texts:
		
		dice_texts = grab_text.split(",")
		dice = {}

		for die in dice_texts:
			try:
				val, key = die.strip().split(" ")
			except ValueError as e:
				print(die)
				print(str(e))
				exit(0)

			dice[key] = int(val)
		grabs.append(dice)
	games.append(grabs)

id_sum = 0

for i, game in enumerate(games):
	is_game_ok = True
	for grab in game:
		for col, num in grab.items():
			# if not all(val < config[key] for key, val in dice.items()):
			if config[col] < num:
				is_game_ok = False
	if is_game_ok:
		id_sum += i + 1

print(id_sum)

id_powers = 0

for i, game in enumerate(games):
	min_config = {
		"red": 1,
		"green": 1,
		"blue": 1
	}

	for grab in game:
		for col, num in grab.items():
			if num > min_config[col]:
				min_config[col] = num
	power = 1
	for num in min_config.values():
		power *= num
	id_powers += power

print(id_powers)
