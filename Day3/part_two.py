import re

def calculate_sum_with_progressive_matching(memory):
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    
    mul_enabled = True
    total_sum = 0
    buffer = ""
    
    for char in memory:
        buffer += char 
        
        if re.findall(do_pattern, buffer):
            mul_enabled = True
            buffer = ""  

        elif re.findall(dont_pattern, buffer):
            mul_enabled = False
            buffer = ""  

        elif mul_enabled and re.findall(mul_pattern, buffer):
            match = re.findall(mul_pattern, buffer)
            total_sum += sum(int(x) * int(y) for x, y in match)
            buffer = ""  

        elif not mul_enabled and re.findall(mul_pattern, buffer):
            mul_enabled = True
            buffer = ""  
    return total_sum

with open("input.txt") as f:
    corrupted_memory = f.read()
result = calculate_sum_with_progressive_matching(corrupted_memory)
print("Sum of valid multiplications (progressive matching):", result)

