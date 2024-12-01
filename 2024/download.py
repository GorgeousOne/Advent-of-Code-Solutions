import sys
import requests

def get_puzzle_input(day, year=2024):
	# load cookie string from secrets.txt
	with open('secrets.txt', 'r') as f:
		session_cookie = f.readline()

	url = f'https://adventofcode.com/{year}/day/{day}/input'
	cookies = {'session': session_cookie}
	response = requests.get(url, cookies=cookies)

	if response.status_code == 200:
		return response.text
	else:
		response.raise_for_status()


if __name__ == '__main__':
	if len(sys.argv) != 2:
		import datetime
		day = datetime.datetime.now().day
	else:
		day = sys.argv[1]

	try:
		day = int(day)
	except ValueError:
		print('Day must be an integer')
		sys.exit(1)
	if day < 1 or day > 25:
		print('Day must be between 1 and 25')
		sys.exit(1)

	puzzle_input = get_puzzle_input(day)
	#print(puzzle_input)
	with open(f'{day:02}input.txt', 'w', encoding='utf-8') as f:
		f.write(puzzle_input)
	num_lines = puzzle_input.count('\n')
	print(f'Downloaded {num_lines} lines of input for day {day}')
