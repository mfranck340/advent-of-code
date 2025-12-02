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

# Calculate the total similarity score
total_similarity_score = 0

for element in list1:
    count = list2.count(element)
    total_similarity_score += element * count

# Print the total similarity score
print("Total similarity score:", total_similarity_score)

