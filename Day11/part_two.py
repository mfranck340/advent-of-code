from concurrent.futures import ProcessPoolExecutor

def len_number(number):
    return len(str(number))

def process_stone(stone):
    tam = len_number(stone)
    if stone == 0:
        return [1]
    elif tam % 2 == 0:
        aux = str(stone)
        return [int(aux[:tam // 2]), int(aux[tam // 2:])]
    else:
        return [stone * 2024]

def split_stones(stones, chunk_size=10000):
    # Dividir la lista en fragmentos
    chunks = [stones[i:i + chunk_size] for i in range(0, len(stones), chunk_size)]
    new_list = []
    with ProcessPoolExecutor() as executor:
        for result in executor.map(process_chunk, chunks):
            new_list.extend(result)
    return new_list

def process_chunk(chunk):
    result = []
    for stone in chunk:
        result.extend(process_stone(stone))
    return result

def read_board(filename):
    with open(filename, 'r') as f:
        return [int(char) for char in f.read().split()]

if __name__ == '__main__':
    map_data = read_board("input.txt")

    print(map_data)
    for i in range(75):
        map_data = split_stones(map_data)
        print(i)

    print("Size of the map: ", len(map_data))
