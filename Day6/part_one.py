import sys
sys.setrecursionlimit(100000)  


def read_board(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def get_count_and_mark(board, pos_ini, ori):
    search_route_and_mark(board, pos_ini[0], pos_ini[1], ori)

def is_finish(board, x, y, ori):
    len_x = len(board)
    len_y = len(board[0])

    if ori == 0 and x == 0:
        return True
    elif ori == 1 and y == len_y - 1:
        return True
    elif ori == 2 and x == len_x - 1:
        return True
    elif ori == 3 and y == 0:
        return True
    return False

def search_route_and_mark(board, x, y, ori):
    board[x][y] = "X"

    if is_finish(board, x, y, ori):
        return
   
    if ori == 0: 
        if board[x - 1][y] == "#":  
            ori = (ori + 1) % 4
            search_route_and_mark(board, x, y, ori)
        else:
            search_route_and_mark(board, x - 1, y, ori)
        
    elif ori == 1:  
        if board[x][y + 1] == "#":  
            ori = (ori + 1) % 4
            search_route_and_mark(board, x, y, ori)
        else:
            search_route_and_mark(board, x, y + 1, ori)
        
    elif ori == 2:  
        if board[x + 1][y] == "#":  
            ori = (ori + 1) % 4
            search_route_and_mark(board, x, y, ori)
        else:
            search_route_and_mark(board, x + 1, y, ori)
        
    elif ori == 3:
        if board[x][y - 1] == "#":
            ori = (ori + 1) % 4
            search_route_and_mark(board, x, y, ori)
        else:
            search_route_and_mark(board, x, y - 1, ori)

# Código principal
filename = "input.txt" 
board = read_board(filename)
board_copy = [row.copy() for row in board]
pos_ini = (86, 45) 
#pos_ini = (6, 4)
ori = 0
get_count_and_mark(board, pos_ini, ori)

count = 0
for row in board:
    for cell in row:
        if cell == "X":
            count += 1

print(count)
for r in board:
    for c in r:
        print(c, end="")
    print()


# Part 2
# Obtener la posicion de las celdas con X
def get_positions(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                positions.append((i, j))
    return positions

def search_loop(board, x, y, ori):
    while True:
        board[x][y] += 1
        
        if board[x][y] == 10:
            return True
        if is_finish(board, x, y, ori):
            return False
        
        if ori == 0: 
            if board[x - 1][y] == "O": 
                ori = (ori + 1) % 4
            elif board[x - 1][y] == "#":  
                ori = (ori + 1) % 4
            else:
                x -= 1  # Moverse hacia arriba
        elif ori == 1:  
            if board[x][y + 1] == "O":  
                ori = (ori + 1) % 4
            elif board[x][y + 1] == "#":  
                ori = (ori + 1) % 4
            else:
                y += 1  # Moverse hacia la derecha
        elif ori == 2:  
            if board[x + 1][y] == "O":
                ori = (ori + 1) % 4
            elif board[x + 1][y] == "#":  
                ori = (ori + 1) % 4
            else:
                x += 1  # Moverse hacia abajo
        elif ori == 3:
            if board[x][y - 1] == "O":
                ori = (ori + 1) % 4
            elif board[x][y - 1] == "#":
                ori = (ori + 1) % 4
            else:
                y -= 1  # Moverse hacia la izquierda

positions_x = get_positions(board)
print(positions_x)
count_loop = 0
for pos_x in positions_x:
    board_cpy_x = [row.copy() for row in board_copy]
    x, y = pos_x
    board_cpy_x[x][y] = "O"

    board_cpy_x[pos_ini[0]][pos_ini[1]] = 0
    for rr in board_cpy_x:
        for cc in rr:
            if cc == ".":
                board_cpy_x[board_cpy_x.index(rr)][rr.index(cc)] = 0

    if search_loop(board_cpy_x, pos_ini[0], pos_ini[1], ori):
        count_loop += 1
        print(x, y)

print(count_loop)