from itertools import product

def evaluate_expression(numbers, operators):
    """Evalúa una expresión de izquierda a derecha, incluyendo el operador de concatenación."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        elif op == "|":
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_valid_equations_with_concat(input_data):
    total_sum = 0

    for line in input_data:
        # Parsear la línea
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        
        # Generar todas las combinaciones posibles de operadores
        num_operators = len(numbers) - 1
        all_operator_combinations = product("+*|", repeat=num_operators)
        
        # Verificar si alguna combinación da el valor objetivo
        valid = False
        for operators in all_operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break
        
        if valid:
            total_sum += target
    
    return total_sum

# Input del ejemplo
example_input = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20"
]

with open("input.txt") as f:
    input_text = f.read().splitlines()

# Calcular la suma total de los valores válidos considerando el operador ||
result = find_valid_equations_with_concat(input_text)
print(f"Resultado total (con ||): {result}")
