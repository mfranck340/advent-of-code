
with open("Day5/input.txt") as f:
	lines = [line.strip() for line in f]  # quita '\n' y espacios

ranges_list = []
while lines and lines[0]:
	line = lines.pop(0)
	start_str, end_str = line.split('-')
	ranges_list.append((int(start_str), int(end_str)))

lines.pop(0)

values = [int(line) for line in lines if line]

# Part 1
count = 0
for value in values:
	for start, end in ranges_list:
		if start <= value <= end:
			count += 1
			break

print(count)

# Part 2
coutn = 0
ranges_list.sort(key=lambda x: x[0])

merged_list = []
for start, end in ranges_list:
	if not merged_list:
		merged_list.append([start, end])

	else:
		last_start, last_end = merged_list[-1]
		if start <= last_end + 1:
			merged_list[-1][1] = max(last_end, end)
		else:
			merged_list.append([start, end])

for start, end in merged_list:
	count += end - start + 1

print(count)