import copy

def simulate_with_obstruction(board, obstruction, pos_ini, ori):
    """Simula el movimiento del guardia con un obstáculo y verifica si entra en un bucle."""
    new_board = copy.deepcopy(board)
    x_obs, y_obs = obstruction
    new_board[x_obs][y_obs] = "#"  # Colocar el obstáculo

    visited = set()
    x, y = pos_ini

    while (x, y) not in visited:
        visited.add((x, y))
        
        if is_finish(new_board, x, y, ori):
            return False  # No hay bucle, llega al borde

        if ori == 0:  # Arriba
            if new_board[x - 1][y] == "#":
                ori = (ori + 1) % 4
            else:
                x -= 1
        elif ori == 1:  # Derecha
            if new_board[x][y + 1] == "#":
                ori = (ori + 1) % 4
            else:
                y += 1
        elif ori == 2:  # Abajo
            if new_board[x + 1][y] == "#":
                ori = (ori + 1) % 4
            else:
                x += 1
        elif ori == 3:  # Izquierda
            if new_board[x][y - 1] == "#":
                ori = (ori + 1) % 4
            else:
                y -= 1

    return True  # Entra en un bucle


def find_loop_positions(board, pos_ini, ori):
    """Encuentra todas las posiciones donde un obstáculo fuerza al guardia a un bucle."""
    loop_positions = []

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == "X":  # Solo considerar posiciones visitadas
                if simulate_with_obstruction(board, (x, y), pos_ini, ori):
                    loop_positions.append((x, y))

    return loop_positions


# Código principal
filename = "test.txt"
board = read_board(filename)
pos_ini = (6, 4)
ori = 0

loop_positions = find_loop_positions(board, pos_ini, ori)

print(f"Total de posiciones que generan bucles: {len(loop_positions)}")
print("Posiciones de bucle:", loop_positions)
