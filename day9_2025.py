data_path = 'day9_2025.txt'

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

rect_area = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[0]):
        if i < j:
            width = abs(matrix[i, 0] - matrix[j, 0]) + 1
            height = abs(matrix[i, 1] - matrix[j, 1]) + 1
            
            rect_area.append(width*height)

print(max(rect_area))

# Part 2
import matplotlib.pyplot as plt



internal_corner_1 = matrix[248]
internal_corner_2 = matrix[249]

print(internal_corner_1)
print(internal_corner_2)



#Check area to each corner:
max_area = 0

for i in range(matrix.shape[0]):
    
    y_pos = matrix[i, 1]
    
    if y_pos > internal_corner_1[1]:
        x_min = min(internal_corner_1[0], matrix[i, 0])
        x_max = max(internal_corner_1[0], matrix[i, 0])
        y_min = min(internal_corner_1[1], matrix[i, 1])
        y_max = max(internal_corner_1[1], matrix[i, 1])
        
        width = x_max - x_min + 1
        height = y_max - y_min + 1
        area = width * height
        
        points_inside_mask = (
            (matrix[:, 0] > x_min) & (matrix[:, 0] < x_max) & 
            (matrix[:, 1] > y_min) & (matrix[:, 1] < y_max)
        )
        
        if not np.any(points_inside_mask):
            if area > max_area:
                max_area = area
                corner_1 = internal_corner_1
                corner_2 = matrix[i]
        
    elif y_pos < internal_corner_2[1]:
        x_min = min(internal_corner_2[0], matrix[i, 0])
        x_max = max(internal_corner_2[0], matrix[i, 0])
        y_min = min(internal_corner_2[1], matrix[i, 1])
        y_max = max(internal_corner_2[1], matrix[i, 1])
        
        width = x_max - x_min + 1
        height = y_max - y_min + 1
        area = width * height
        
        points_inside_mask = (
            (matrix[:, 0] > x_min) & (matrix[:, 0] < x_max) & 
            (matrix[:, 1] > y_min) & (matrix[:, 1] < y_max)
        )
        
        if not np.any(points_inside_mask):
            if area > max_area:
                max_area = area
                corner_1 = internal_corner_2
                corner_2 = matrix[i]

print(max_area)

plt.scatter(matrix[:, 0]/100, matrix[:, 1]/100)
plt.scatter(corner_1[0]/100, corner_1[1]/100)
plt.scatter(corner_2[0]/100, corner_2[1]/100)
plt.show()



    ## store all edge positions
    
## Iterate through all rectangle pairs and make sure the 4 corners are on edges