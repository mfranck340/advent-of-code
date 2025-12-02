antenna_dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def read_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def create_void_board(board):
    return [["." for _ in range(len(board[0]))] for _ in range(len(board))]

def find_antennas(board):
    """Encuentra todas las posiciones de las antenas en el tablero y las agrupa por frecuencia."""
    antennas = {freq: [] for freq in antenna_dict}
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell in antenna_dict:
                antennas[cell].append((x, y))
    return antennas

def calculate_antinodes(antennas, board_dim):
    """Calcula las posiciones de los antinodos para todas las antenas del tablero."""
    antinodes = set()
    width, height = board_dim

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue

        print(f"Calculating antinodes for antenna {freq}...")

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calcular los antinodos (doble distancia)
                dx, dy = x2 - x1, y2 - y1
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Añadir antinodos si están dentro de los límites
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)

    return antinodes

def mark_antinodes(board_void, antinodes):
    """Marca las posiciones de los antinodos en el tablero vacío."""
    for x, y in antinodes:
        board_void[y][x] = '#'
    return board_void

def count_unique_antinode_positions(antinodes, board):
    """Cuenta las posiciones únicas que contienen antinodos en el tablero."""
    unique_positions = set(antinodes)

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell in antenna_dict and (x, y) in unique_positions:
                unique_positions.add((x, y))

    return len(unique_positions)

# Código principal
filename = "test.txt"
board = read_board(filename)
board_void = create_void_board(board)

# Paso 1: Encontrar antenas
antennas = find_antennas(board)
print(antennas)

# Paso 2: Calcular antinodos
antinodes = calculate_antinodes(antennas, (len(board[0]), len(board)))

# Paso 3: Marcar antinodos
board_void = mark_antinodes(board_void, antinodes)

# Paso 4: Contar posiciones únicas
unique_count = count_unique_antinode_positions(antinodes, board)

print(f"Total unique antinode positions: {unique_count}")

for row in board_void:
    for cell in row:
        print(cell, end="")
    print()
