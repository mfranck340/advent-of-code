def count_paths(map_data, position, memo):
    """Count all unique paths from the current position to any 9."""
    rows, cols = len(map_data), len(map_data[0])
    x, y = position

    # Check if we reached a height of 9
    if map_data[x][y] == 9:
        return 1

    # Use memoized results if available
    if position in memo:
        return memo[position]

    total_paths = 0
    current_height = map_data[x][y]

    # Explore neighbors (up, down, left, right)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            next_height = map_data[nx][ny]
            if next_height == current_height + 1:
                total_paths += count_paths(map_data, (nx, ny), memo)

    # Memoize the result for the current position
    memo[position] = total_paths
    return total_paths

def calculate_ratings(map_data):
    """Calculate the sum of ratings for all trailheads."""
    trailheads = find_trailheads(map_data)
    total_rating = 0

    for trailhead in trailheads:
        # Use memoization to store results for visited positions
        memo = {}
        total_rating += count_paths(map_data, trailhead, memo)
    
    return total_rating

def find_trailheads(map_data):
    """Find all positions with height 0 in the map."""
    trailheads = []
    for r, row in enumerate(map_data):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads


def parse_input(input_str):
    """Parse the input topographic map into a 2D list."""
    return [list(map(int, line.strip())) for line in input_str.splitlines()]
example_input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
map_data = parse_input(example_input)

def read_board(filename):
    with open(filename, 'r') as f:
        return [[int(char) for char in line.strip()] for line in f.readlines()]
    
map_data = read_board("input.txt")

# Calculate the sum of ratings for the example input
rating = calculate_ratings(map_data)
print(rating)
