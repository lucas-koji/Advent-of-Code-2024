left = []
right = []
with open('input.txt', 'r') as file:
	for row in file:
		values = row.strip().split('   ')
		left.append(int(values[0]))
		right.append(int(values[1]))
left.sort()
right.sort()
total = 0
for i in range(len(left)):
	current = left[i] - right[i]
	if current < 0:
		current = -current
	total += current
print(total)
