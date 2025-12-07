data_path = 'day7_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 
import numpy as np

data = np.array(data)

matrix = []

for row in data:
    matrix.append(list(row))
    
matrix = np.array(matrix)



matrix[matrix == '.'] = 0
matrix[matrix == 'S'] = 1
matrix[matrix == '^'] = 2

matrix = matrix.astype(int)

matrix[matrix == 2] = -1

split_count = 0

for i in range(1, matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i-1, j] == 1:
            if matrix[i, j] == -1:         
                matrix[i, j-1] = 1
                matrix[i, j+1] = 1
                split_count += 1
            else:
                matrix[i,j] = 1
                
print(split_count)
                
#Part 2:
data = np.array(data)

matrix = []

for row in data:
    matrix.append(list(row))
    
matrix = np.array(matrix)



matrix[matrix == '.'] = 0
matrix[matrix == 'S'] = 1
matrix[matrix == '^'] = 2

matrix = matrix.astype(int)

matrix[matrix == 2] = -1

laser_matrix = np.zeros_like(matrix).astype(np.int64)

laser_matrix[matrix == 1] = 1


for i in range(1, matrix.shape[0]):
    
    new_row = np.zeros(matrix.shape[1]).astype(np.int64)
    
    for j in range(matrix.shape[1]):
        
        upstream = laser_matrix[i-1, j]

        left_neighbor = matrix[i, j-1] if j > 0 else 0
        right_neighbor = matrix[i, j+1] if j < matrix.shape[1] - 1 else 0
        
        if upstream > 0:
            if matrix[i, j] == -1:
                if j > 0:
                    new_row[j-1] += upstream
                if j < matrix.shape[1] - 1:
                    new_row[j+1] += upstream
            else:
                new_row[j] += upstream
                
    laser_matrix[i, :] = new_row
    
print(laser_matrix[-1, :])
                
print(sum(laser_matrix[-1, :]))

#Todo, check to see if there are splitters on both sides and add the upstream, otherwise overwrite the laser to the upstream