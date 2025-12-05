data_path = 'day5_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 

split_reached = False

range_list = []
ingredient_list = []

valid_ingredients = 0

for row in data:
    if row == '':
        split_reached = True
    if not split_reached:
        range_list.append(row)
    elif row != '':
        ingredient_list.append(row)
        

for ingredient in ingredient_list:
    id = int(ingredient)
    for id_range in range_list:
        id_range = id_range.split('-')
        if (id >= int(id_range[0])) & (id <= int(id_range[1])):
            valid_ingredients += 1
            break
            
print(valid_ingredients)

# Part 2
index_array = []

for id_range in range_list:
    id_range = id_range.split('-')
    index_array.append([int(id_range[0]), int(id_range[1])])
    
index_array.sort()

combined_index = []

for start, end in index_array:
    
    if combined_index == []:
        combined_index.append([start, end])
    elif start > combined_index[-1][1]:
        combined_index.append([start, end])
    else:
        combined_index[-1][1] = max(combined_index[-1][1], end)
        
valid_ids = 0

for id_range in combined_index:
    valid_ids += (id_range[1] - id_range[0] + 1)
    
print(valid_ids)
