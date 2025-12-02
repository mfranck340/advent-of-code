

def len_number(number):
    return len(str(number))

def split_stones(stones):
    new_list = []
    for i in range(len(stones)):
        tam = len_number(stones[i])
        if stones[i] == 0:
            new_list.append(1)
        elif tam % 2 == 0:
            aux = str(stones[i])
            new_list.append(int(aux[:tam//2]))
            new_list.append(int(aux[tam//2:]))
        else:
            new_list.append(stones[i] * 2024) 
    return new_list

def read_board(filename):
    with open(filename, 'r') as f:
        return [int(char) for char in f.read().split()] 
    
map_data = read_board("input.txt")

print(map_data)
for i in range (75):
    map_data = split_stones(map_data)
    print(i)


print("Size of the map: ", len(map_data))