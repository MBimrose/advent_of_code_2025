data_path = 'day8_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 
import numpy as np

from scipy.spatial.distance import cdist

data = np.array(data)

matrix = []

for row in data:
    matrix.append(row.split(','))
    
matrix = np.array(matrix).astype(int)

diffs_squared = (matrix[:, np.newaxis, :] - matrix[np.newaxis, :, :])**2
# Sum the squared differences along the coordinate axis and take the square root
distances_matrix = np.sqrt(np.sum(diffs_squared, axis=2))

np.fill_diagonal(distances_matrix, np.inf)

print(distances_matrix)

group_array = []

for i in range(1000):
    min_index = (np.argmin(distances_matrix))
    min_row, min_col = np.unravel_index(min_index, distances_matrix.shape)
    
    distances_matrix[min_row, min_col] = np.inf
    distances_matrix[min_col, min_row] = np.inf
    
    new_group = True
    
    groups_to_merge = []
    other_groups = []
    
    for group in group_array:
        # Check if this group contains EITHER of our points
        if min_row in group or min_col in group:
            groups_to_merge.append(group)
        else:
            other_groups.append(group)
    
    if len(groups_to_merge) == 0:
        other_groups.append({min_row, min_col})
    
    else:
        merged_group = {min_row, min_col}
        for group in groups_to_merge:
            merged_group.update(group)
        other_groups.append(merged_group)
        
    group_array = other_groups
    
group_lengths = []
    
for group in group_array:
    group_lengths.append(len(group))
    
group_lengths.sort(reverse=True)

print(group_lengths)
print(group_lengths[:3])

print(np.prod(group_lengths[:3]))

#Part 2:
import numpy as np

from scipy.spatial.distance import cdist

data = np.array(data)

matrix = []

for row in data:
    matrix.append(row.split(','))
    
matrix = np.array(matrix).astype(int)

diffs_squared = (matrix[:, np.newaxis, :] - matrix[np.newaxis, :, :])**2
# Sum the squared differences along the coordinate axis and take the square root
distances_matrix = np.sqrt(np.sum(diffs_squared, axis=2))

np.fill_diagonal(distances_matrix, np.inf)

print(distances_matrix)

group_array = []

groups_united = False

while not groups_united:
    min_index = (np.argmin(distances_matrix))
    min_row, min_col = np.unravel_index(min_index, distances_matrix.shape)
    
    distances_matrix[min_row, min_col] = np.inf
    distances_matrix[min_col, min_row] = np.inf
    
    new_group = True
    
    groups_to_merge = []
    other_groups = []
    
    for group in group_array:
        # Check if this group contains EITHER of our points
        if min_row in group or min_col in group:
            groups_to_merge.append(group)
        else:
            other_groups.append(group)
    
    if len(groups_to_merge) == 0:
        other_groups.append({min_row, min_col})
    
    else:
        merged_group = {min_row, min_col}
        for group in groups_to_merge:
            merged_group.update(group)
        other_groups.append(merged_group)
        
    group_array = other_groups
    
    print(len(group_array))
    
    if (len(group_array) == 1) & (len(group_array[0]) == 1000):
        groups_united = True
        
        print(matrix[min_col, 0] * matrix[min_row, 0])