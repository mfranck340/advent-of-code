# Challenge 4

def read_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def search_word(board, word):
    """Buscar la palabra en el tablero en todas las direcciones."""
    rows, cols = len(board), len(board[0])
    directions = [
        (0, 1), (0, -1),  # Horizontal
        (1, 0), (-1, 0),  # Vertical
        (1, 1), (-1, -1), # Diagonal principal
        (1, -1), (-1, 1)  # Diagonal secundaria
    ]
    word_len = len(word)
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(word_len):
                    nr, nc = r + dr * i, c + dc * i
                    if not is_valid(nr, nc) or board[nr][nc] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count

# Main
filename = "input.txt"  # Nombre del archivo con el tablero
board = read_board(filename)
word = "XMAS"
result = search_word(board, word)
print(f"La palabra '{word}' aparece {result} veces en el tablero.")
