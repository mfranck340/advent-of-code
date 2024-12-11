from collections import defaultdict, deque

def find_middle_page(update):
    """Finds the middle page of the update."""
    return update[len(update) // 2]

def build_graph(rules):
    """Builds a directed graph from the rules."""
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph

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

def is_valid_update(update, graph):
    """Checks if an update is valid based on the graph."""
    index_map = {page: i for i, page in enumerate(update)}
    for x in graph:
        for y in graph[x]:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:
                    return False
    return True

def correct_update(update, graph):
    """Corrects the order of an update based on the graph."""
    subset = set(update)
    local_graph = {node: [] for node in subset}
    local_indegree = {node: 0 for node in subset}

    # Construir grafo local y grados de entrada
    for x in graph:
        for y in graph[x]:
            if x in subset and y in subset:
                local_graph[x].append(y)
                local_indegree[y] += 1

    # Ordenación topológica
    queue = deque([node for node in subset if local_indegree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in local_graph[node]:
            local_indegree[neighbor] -= 1
            if local_indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def solve_puzzle_part_two(input_text):
    """Solves the second part of the puzzle."""
    rules, updates = parse_rules_and_updates(input_text)
    graph = build_graph(rules)
    
    total = 0
    for update in updates:
        if not is_valid_update(update, graph):
            corrected_update = correct_update(update, graph)
            total += find_middle_page(corrected_update)
    
    return total

# Leer archivo y resolver
with open("input.txt") as f:
    input_text = f.read()

result_part_two = solve_puzzle_part_two(input_text)
print(f"Sum of middle pages from corrected updates: {result_part_two}")

#12020
