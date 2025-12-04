data_path = 'day4_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 

import numpy as np
from scipy.signal import convolve2d

data = np.array(data)

matrix = []

for row in data:
    matrix.append(list(row))
    
matrix = np.array(matrix)

matrix[matrix == '.'] = 0
matrix[matrix == '@'] = 1

matrix = matrix.astype(int)

kernel = np.array([[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]).astype(int)

convolved_array = convolve2d(matrix, kernel, mode='same')

accessible_rolls = np.sum(convolved_array[matrix == 1] < 4)


print(accessible_rolls)

# Part 2

total_rolls = 0

while accessible_rolls > 0:
    convolved_array = convolve2d(matrix, kernel, mode='same')

    accessible_rolls = np.sum(convolved_array[matrix == 1] < 4)
    
    print(accessible_rolls)
    
    total_rolls += accessible_rolls
    
    
    matrix[(convolved_array < 4) & (matrix == 1)] = 0
    
    
print(total_rolls)

