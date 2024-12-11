from collections import deque

def parse_input(input_str):
    """Parse the input topographic map into a 2D list."""
    return [list(map(int, line.strip())) for line in input_str.splitlines()]

def find_trailheads(map_data):
    """Find all positions with height 0 in the map."""
    trailheads = []
    for r, row in enumerate(map_data):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def bfs(map_data, start):
    """Perform BFS from the given start position to find reachable 9s."""
    rows, cols = len(map_data), len(map_data[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        current_height = map_data[x][y]

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited:
                    next_height = map_data[nx][ny]
                    if next_height == current_height + 1:
                        if next_height == 9:
                            reachable_nines.add((nx, ny))
                        queue.append((nx, ny))
                        visited.add((nx, ny))
    
    return reachable_nines

def calculate_scores(map_data):
    """Calculate the sum of scores for all trailheads."""
    trailheads = find_trailheads(map_data)
    total_score = 0

    for trailhead in trailheads:
        reachable_nines = bfs(map_data, trailhead)
        total_score += len(reachable_nines)
    
    return total_score

# Example input
example_input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def read_board(filename):
    with open(filename, 'r') as f:
        return [[int(char) for char in line.strip()] for line in f.readlines()]
    
map_data = read_board("input.txt")

# Process example input
#map_data = parse_input(example_input)
score = calculate_scores(map_data)
print(score)
