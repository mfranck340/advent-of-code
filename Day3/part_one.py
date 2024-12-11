#Challenge 3

import re

# Función para analizar la memoria corrupta y calcular el resultado
def calculate_sum_of_multiplications(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, memory)
    
    # Calcular la suma de las multiplicaciones
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

# Leer el archivo de memoria corrupta
with open("input.txt") as f:
    corrupted_memory = f.read()

# Calcular el resultado
result = calculate_sum_of_multiplications(corrupted_memory)
print("Sum of valid multiplications:", result)
