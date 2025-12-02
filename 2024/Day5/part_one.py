from collections import defaultdict, deque

def parse_rules_and_updates(input_text):
    """Parses the input text into rules and updates."""
    sections = input_text.strip().split("\n\n")
    rules_section = sections[0].splitlines()
    updates_section = sections[1].splitlines()

    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split('|'))
        rules.append((x, y))
    
    updates = []
    for update in updates_section:
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def build_graph(rules):
    """Builds a directed graph from the rules."""
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph

def is_valid_update(update, graph):
    """Checks if an update is valid based on the graph."""
    index_map = {page: i for i, page in enumerate(update)}
    for x in graph:
        for y in graph[x]:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:
                    return False
    return True

def find_middle_page(update):
    """Finds the middle page of the update."""
    return update[len(update) // 2]

def solve_puzzle(input_text):
    """Solves the puzzle and returns the sum of middle pages of valid updates."""
    rules, updates = parse_rules_and_updates(input_text)
    graph = build_graph(rules)
    
    total = 0
    for update in updates:
        if is_valid_update(update, graph):
            total += find_middle_page(update)
    
    return total

with open("input.txt") as f:
    input_text = f.read()

# Solve and print the result
result = solve_puzzle(input_text)
print(f"Sum of middle pages from valid updates: {result}")
