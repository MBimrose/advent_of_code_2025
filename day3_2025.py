data_path = 'day3_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1  
joltage_sum = 0

for row in data:
    array = [int(digit) for digit in row]
    joltage_values = []
    for i in range(len(array)):
        for j in range(len(array)):
            joltage = int("".join(map(str, [array[i], array[j]])))
            if i < j:
                joltage_values.append(joltage)
    
    highest_joltage = max(joltage_values)
    
    joltage_sum += highest_joltage

print(joltage_sum)

# Part 2
joltage_sum = 0
# print(data)
for row in data:
    print(row)
    digit_array = []
    array = [int(digit) for digit in row]
    
    start_index = 0
    
    search_array = array
    
    for i in reversed(range(0,12)):
        search_array = search_array[start_index:]
        if i > 0:
            search = search_array[:-i]
        else:
            search = search_array
        max_digit = max(search)
        start_index = search.index(max_digit) + 1
        digit_array.append(max_digit)

    joltage = int("".join(map(str, digit_array)))
    print(joltage)

    joltage_sum += joltage
    
print(joltage_sum)


