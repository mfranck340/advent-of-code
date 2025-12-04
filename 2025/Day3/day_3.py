# DAY 3
with open("Day3/input.txt") as f:
    banks = [line.strip() for line in f]  # quita '\n' y espacios

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




