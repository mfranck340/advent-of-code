# DAY 3
with open("Day3/input.txt") as f:
	banks = [line.strip() for line in f]

# Part 1
result = 0

for bank in banks:
	max_joltage = 0
	for i in range(len(bank) - 1):
		if int(bank[i]) >= max_joltage // 10:
			aux = int(bank[i]) * 10
			for j in range(i + 1, len(bank)):
				if aux + int(bank[j]) > max_joltage:
					max_joltage = aux + int(bank[j])
	result += max_joltage

print(result)

# Part 2
import numpy as np

with open("Day3/input.txt") as f:
	banks = np.array([[int(c) for c in line.strip()] for line in f])

result = 0
ini = 0
digits = 11
for bank in banks:
	max_joltage = 0

	for dig in range(12):
		max = 0

		for i in range(ini, len(bank) - digits):
			if bank[i] > max:
				max = bank[i]
				ini = i + 1
		digits -= 1
		max_joltage = (max_joltage * 10) + max

	result += max_joltage
	digits = 11
	ini = 0

print(result)
