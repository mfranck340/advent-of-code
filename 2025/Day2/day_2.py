

file = open("Day2/input.txt", "r")
ranges = file.readlines()[0].split(",")
result = 0

for range_id in ranges:
    min_id, max_id = map(int, range_id.split("-"))

    for num in range(min_id, max_id + 1):
        cad = str(num)
        if num < 10:
            continue
        else:
            middle = int(len(cad) / 2)

            for mid_aux in range(1, middle + 1):
                is_symmetric = True
                for i in range(0, len(cad) - mid_aux, mid_aux):
                    j = i + mid_aux
                    if cad[i: j] != cad[j: j + mid_aux]:
                        is_symmetric = False
                        break
                if is_symmetric:
                    break

            if is_symmetric:
                #print(f"range_id: {range_id} num: {num} cad: {cad} mid_aux: {mid_aux}")
                result += num

print(result)