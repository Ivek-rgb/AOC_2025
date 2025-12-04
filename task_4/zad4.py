from copy import deepcopy 

moves_x = [1,1,1,0,0,-1,-1,-1]
moves_y = [1,-1,0,1,-1,1,-1,0]

def is_inbounds(bounds : tuple[int], coords : tuple[int]): 
    bounds_y, bounds_x = bounds
    y, x = coords
    return y >= 0 and y < bounds_y and x >= 0 and x < bounds_x

"""
def do_adjecents_action(start_coords : tuple[int], bounds : tuple[int], action : function): 
    start_y, start_x = start_coords
    for i in range(len(moves_x)):
        srch_x = start_x + moves_x[i]
        srch_y = start_y + moves_y[i]
        if is_inbounds(bounds, (srch_y, srch_x)): 
            action(srch_y, srch_x) 
"""
         
def main(): 
    with open("./test.txt", "r") as file: 
        lines = file.read().splitlines()
        for i in range(len(lines)): 
            lines[i] = [*lines[i]]
    
        count = 0
        bounds = (len(lines), len(lines[0]))
        
        row = [0] * bounds[1]
        count_matrix = [deepcopy(row) for _ in range(bounds[0])] 
         
        """ Part 1. 
        for i in range(len(lines)): 
            for j in range(len(lines[i])): 
                reachable_count = 0
                if lines[i][j] in ("@", "x"): 
                    for k in range(len(moves_x)): 
                        srch_x = j + moves_x[k]
                        srch_y = i + moves_y[k]
                        if is_inbounds(bounds, (srch_y, srch_x)) and lines[srch_y][srch_x] in ('@', 'x'):
                            reachable_count += 1
                    if reachable_count < 4: 
                        lines[i][j] = '.'
                        count += 1  
        """
        
        queue = []
        for i in range(len(lines)): 
            for j in range(len(lines[i])): 
                reachable_count = 0
                if lines[i][j] in ("@", "x"): 
                    for k in range(len(moves_x)): 
                        srch_x = j + moves_x[k]
                        srch_y = i + moves_y[k]
                        if is_inbounds(bounds, (srch_y, srch_x)) and lines[srch_y][srch_x] in ('@', 'x'):
                            reachable_count += 1
                    count_matrix[i][j] = reachable_count
                    if(reachable_count < 4):
                        count_matrix[i][j] = -1 
                        queue.append((i,j))
        
        
        while len(queue): 
            inter_y, inter_x = queue.pop(0)
            count += 1 
            for i in range(len(moves_x)): 
                adj_x = inter_x + moves_x[i]
                adj_y = inter_y + moves_y[i]
                if is_inbounds(bounds, (adj_y, adj_x)) and lines[adj_y][adj_x] in ('@', 'x'): 
                    count_matrix[adj_y][adj_x] -= 1 
                    if count_matrix[adj_y][adj_x] < 4 and count_matrix[adj_y][adj_x] > 0:
                        queue.append((adj_y, adj_x))
                        count_matrix[adj_y][adj_x] = -1
        print(count)


  
            
                        
                        
                        
                        
                        
                    
                    
                
                
                


main() 
