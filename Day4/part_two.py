def read_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def check_pattern(board, r, c, offsets):
    rows, cols = len(board), len(board[0])
    for dr, dc, char in offsets:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < rows and 0 <= nc < cols) or board[nr][nc] != char:
            return False
    return True

def search_rotated_patterns(board):
    rows, cols = len(board), len(board[0])
    count = 0

    # Todas las rotaciones del patrón
    patterns = [
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],  # Original
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],  # Rotada 90°
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],  # Rotada 180°
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],  # Rotada 270°
    ]

    for r in range(1, rows - 1):  # Excluir bordes
        for c in range(1, cols - 1):  # Excluir bordes
            if board[r][c] == 'A':  # El centro debe ser 'A'
                for pattern in patterns:
                    if check_pattern(board, r, c, pattern):
                        count += 1
                        break 

    return count

# Main
filename = "input.txt"  # Nombre del archivo con el tablero
board = read_board(filename)
result = search_rotated_patterns(board)
print(f"El patrón en forma de 'X' (con rotaciones) aparece {result} veces en el tablero.")
