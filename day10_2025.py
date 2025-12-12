data_path = 'day10_2025.txt'

with open(data_path) as f:
    data = f.read().split('\n')
  
# Part 1 

# import re
# import math

# total_button_presses = 0

# for row in data:
#     if not row.strip():
#         continue
#     parts = row.split()
#     target_state = parts[0][1:-1]
#     target_state = [-1 if switch == '.' else 1 if switch == '#' else 0 for switch in target_state]
#     button_str = parts[1:-1]
#     button_array = []
#     for button in button_str:
#         button_seq = button[1:-1].split(',')
#         button_array.append([int(b) for b in button_seq])
        
#     current_states = [[-1]*len(target_state)]
#     next_states = [[-1]*len(target_state)]
    
#     buttons_presses = 0
    
#     current_states = next_states
    
#     while target_state not in current_states:
        
#         next_states = []
#         for state in current_states:
#             for button in button_array:
#                 button_state = [1]*len(target_state)
#                 for index in button:
#                     button_state[index] = -1
#                 new_state = [x * y for x, y in zip(button_state, state)]
#                 next_states.append(new_state)
                
#         current_states = next_states
                
#         buttons_presses += 1

        
#     print(buttons_presses)
            
#     total_button_presses += buttons_presses
        
        
    

# print(total_button_presses)

#Part 2
from z3 import *

button_press_total = 0

for row in data:
    parts = row.split(' ')
    target_state = parts[-1][1:-1].split(',')
    target_state = [int(b) for b in target_state]
    button_str = parts[1:-1]
    button_array = []
    for button in button_str:
        button_seq = button[1:-1].split(',')
        button_array.append([int(b) for b in button_seq])
        
    X = IntVector('x', len(button_array))
    opt = Optimize()
    
    for x in X:
        opt.add(x >= 0)
    
    for i in range(len(target_state)):
        button_inclusion = [0]*len(button_array)
        for j in range(len(button_array)):
            if i in button_array[j]:
                button_inclusion[j] = 1
        # use explicit dot product between button_inclusion (0/1) and X
        opt.add(sum(button_inclusion[j] * X[j] for j in range(len(button_array))) == target_state[i])
        
    total_presses = Sum(X)
    opt.minimize(total_presses)
            
    if opt.check() == sat:
        m = opt.model()
        row_total = m.eval(total_presses).as_long()
        print(f"Minimum presses for row: {row_total}")
        button_press_total += row_total
    else:
        print("No solution found for row.")

print(button_press_total)