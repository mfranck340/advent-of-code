# DAY 4

# Part 1
with open("Day4/input.txt") as f:
	map = [line.strip() for line in f]  # quita '\n' y espacios

map_aux = [list(row) for row in map]

def check_condition(row: int, col: int, map: list[list[str]]) -> bool:
	count_aux = 0
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
				  (-1, -1), (-1, 1), (1, -1), (1, 1)]
	for dr, dc in directions:
		r, c = row + dr, col + dc
		if 0 <= r < len(map) and 0 <= c < len(map[0]):
			if map[r][c] == '@':
				count_aux += 1
	return count_aux < 4

for row in range(len(map)):
	for col in range(len(map[0])):
		if map[row][col] == '@' and check_condition(row, col, map):
			map_aux[row][col] = 'X'

count = 0
for row in range(len(map)):
	for col in range(len(map[0])):
		if map_aux[row][col] == 'X':
			count += 1

print(count)

# Part 2
with open("Day4/input.txt") as f:
	map = [line.strip() for line in f]  # quita '\n' y espacios

map_aux = [list(row) for row in map]

def check_condition(row: int, col: int, map: list[list[str]]) -> bool:
	count_aux = 0
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
				  (-1, -1), (-1, 1), (1, -1), (1, 1)]
	for dr, dc in directions:
		r, c = row + dr, col + dc
		if 0 <= r < len(map) and 0 <= c < len(map[0]):
			if map[r][c] == '@':
				count_aux += 1
	return count_aux < 4

total_count = 0

while True:

	for row in range(len(map)):
		for col in range(len(map[0])):
			if map[row][col] == '@' and check_condition(row, col, map):
				map_aux[row][col] = 'X'

	count = 0
	for row in range(len(map)):
		for col in range(len(map[0])):
			if map_aux[row][col] == 'X':
				count += 1

	for row in range(len(map)):
		for col in range(len(map[0])):
			if map_aux[row][col] == 'X':
				map_aux[row][col] = '.'

	if count == 0:
		break

	total_count += count
	map = [list(r) for r in map_aux]
	# print("ACTUAL MAP\n")
	# for r in map:
	# 	print("".join(r))
	# print("\n\n\n")

print(total_count)



