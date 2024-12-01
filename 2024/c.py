import datetime
import os
import sys
import shutil

if len(sys.argv) < 2:
	day = datetime.datetime.now().day
else:
	day = sys.argv[1]

try:
	day_int = int(day)
except ValueError:
	print("The provided day number is not an integer.")
	sys.exit(1)

source_file = f"day{day_int}.py"
destination_file = f"day{day_int}b.py"

if os.path.isfile(destination_file):
	print(f"The file {destination_file} already exists.")
	sys.exit(1)

try:
	shutil.copy(source_file, destination_file)
	print(f"Copied {source_file} to {destination_file}")
except FileNotFoundError:
	print(f"The file {source_file} does not exist.")
except Exception as e:
	print(f"An error occurred: {e}")