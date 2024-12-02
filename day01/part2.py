left = []
right = {}
with open('input.txt', 'r') as file:
	for row in file:
		[l, r] = row.strip().split('   ')
		l, r = int(l), int(r)
		left.append(l)
		right[r] = right.get(r, 0) + 1
total = 0
for l in left:
	total += l * right.get(l, 0)
print(total)
