import re

with open("input.txt", "r") as file:
    content = file.read()

matches = re.findall(r"mul\((\d+),\s*(\d+)\)", content)
total = 0

for x, y in matches:
	total += int(x) * int(y)

print(f'part1: {total}')
