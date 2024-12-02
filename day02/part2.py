def safetyValidation(row):
	arr = []
	count = 0
	for i in range(1, len(row)):
		arr.append(int(row[i]) - int(row[i - 1]))
	positive, negative = 0, 0
	for i in range(len(arr)):
		if arr[i] == 0:
			return False
		if abs(arr[i]) > 3:
			return False
		if arr[i] > 0:
			positive += 1
		else:
			negative += 1
	return positive == 0 or negative == 0


total = 0
with open('input.txt', 'r') as file:
	for row in file:
		values = [int(val) for val in row.strip().split(' ')]
		if safetyValidation(values):
			total += 1
			continue
		for i in range(len(values)):
			current = values[:i] + values[i + 1:]
			safety = safetyValidation(current)
			if safety:
				total += 1
				break
print(total)
