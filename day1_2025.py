
data_path = 'day1_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
    
print(data)

position = 50

zero_count = 0

for move in data:
    direction = move[0]
    tick_num = int(move[1:])
    
    start_position = position
    
    if direction == 'R':
        position += tick_num
    else:
        position -= tick_num
        
    if (position % 100) == 0:
        zero_count += 1
        
    position = position % 100

        
print(zero_count)

position = 50

zero_count = 0

for move in data:
    direction = move[0]
    tick_num = int(move[1:])
    
    start_position = position
    
    if direction == 'R':
        position += tick_num
        
        zero_count += (position // 100)
        
    else:
        position -= tick_num
        
        zero_count += abs((position-1) // 100)
        
        if start_position == 0:
            zero_count -= 1
        
    position = position % 100

        
print(zero_count)