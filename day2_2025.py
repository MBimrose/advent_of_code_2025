
data_path = 'day2_2025.txt'

with open(data_path) as f:
    data = f.read().split(',')

print(data)
    
invalid_total = 0
    
for row in data:
    num1, num2 = row.split('-')
    
    
    for id in range(int(num1), int(num2)+1):
        # print(id)
        id = str(id)
        for i in range(1, len(id)//2 + 1):
            test_pattern = id[:i]
            sequence_freq = id.count(test_pattern)
            if (test_pattern * sequence_freq) == id:
                invalid_total += int(id)
                print(id)
                break


print(invalid_total)
