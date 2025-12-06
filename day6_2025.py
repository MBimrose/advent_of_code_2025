data_path = 'day6_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 

import numpy as np
import math

filter_data = []

for i, row in enumerate(data):
    filtered_row = []
    row = row.split(' ')
    for item in row:
        if item != '':
            filtered_row.append(item)
            
    filter_data.append(filtered_row)
    
filter_data = np.array(filter_data)

total_math = 0

print(len(filter_data[0]))
print(len(filter_data))

for i in range(len(filter_data[0])):
    if filter_data[-1][i] == '+':
        total_math += np.sum(filter_data[:-1, i].astype(np.int64))
    if filter_data[-1][i] == '*':
        total_math += np.prod(filter_data[:-1, i].astype(np.int64))
            
print(total_math)


# Part 2
total_math = 0

filter_data = []

for row in data:
    np_row = np.array(list(row))
    filter_data.append(np_row)
    
filter_data = np.array(filter_data)

print(filter_data)

column_divider_array = []

for i in range(filter_data.shape[1]):
    if np.all(filter_data[:, i] == ' '):
        column_divider_array.append(i)
        
column_divider_array.append(filter_data.shape[1])

for i in range(len(column_divider_array)):
    if i == 0:
        raw_equation = filter_data[:, :column_divider_array[i]]
    else:
        raw_equation = filter_data[:, (column_divider_array[i-1] + 1):column_divider_array[i]]
        
       
    numbers = []
    del_values = [' ', '+', '*']
        
    for j in range(raw_equation.shape[1]):
        col = raw_equation[:, j]
        col = col[~np.isin(col, del_values)]
        numbers.append(int(''.join(col)))
    
    operator = raw_equation[-1, 0]
    
    if operator == '+':
        total_math += np.sum(numbers)
    elif operator == '*':
        total_math += np.prod(numbers, dtype=np.int64)
    else:
        print('invalid')
        print(raw_equation)

        
print(total_math)