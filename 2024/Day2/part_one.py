#Challenge 2

def is_safe(report):
    # Verifica si los niveles son todos crecientes o decrecientes
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if all(1 <= diff <= 3 for diff in differences):  # Creciente
        return True
    if all(-3 <= diff <= -1 for diff in differences):  # Decreciente
        return True
    return False

def is_safe_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Eliminar un nivel
        if is_safe(modified_report):
            return True
    return False

# Leer los informes del archivo
safe_count = 0
with open("input.txt") as f:
    for line in f:
        report = list(map(int, line.split()))  # Convierte la línea en una lista de enteros
        if is_safe(report):
            safe_count += 1
        else:
            if is_safe_dampener(report):
                safe_count += 1

print("Number of safe reports:", safe_count)
