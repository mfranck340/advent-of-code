
# DAY 1
# First part
ft = open("data_day_1.txt", "r")
lines = ft.readlines()

MIN = 0
MAX = 100

count = 0
actual = 50

for line in lines:
	if 'L' in line:
		number = int(line[1:])
		actual = (actual - number) % MAX
	elif 'R' in line:
		number = int(line[1:])
		actual = (actual + number) % MAX

	if actual == MIN:
		count += 1

print("Final count:", count)

# Second part
ft = open("data_day_1.txt", "r")
lines = ft.readlines()

MIN = 0
MAX = 100

count = 0
actual = 50

for line in lines:
	number = int(line[1:])
	aux = number % MAX
	times = number // MAX
	count += times

	if 'L' in line:
		if actual > 0 and aux >= actual:
			count += 1
		actual = (actual - number) % MAX
	elif 'R' in line:
		if aux > 0 and aux + actual >= MAX:
			count += 1
		actual = (actual + number) % MAX

print("Final count:", count)
