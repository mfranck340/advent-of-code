#Challenge 1
list1 = []
list2 = []

# Read the input file
with open('input.txt') as f:
    lines = f.readlines()
    
for line in lines:
    number =line.split()
    list1.append(int(number[0]))
    list2.append(int(number[1]))

list1.sort()
list2.sort()

result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])

print(result)

