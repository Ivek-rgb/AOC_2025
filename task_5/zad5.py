
def main(): 
    with open("./test.txt", "r") as file: 
        lines = file.read().splitlines()
        split_idx = lines.index('')
        ranges =  sorted([tuple(map(lambda x: int(x),range.split('-'))) for range in lines[:split_idx]], key=lambda x: x[0])
        indexes = list(map(lambda x: int(x),lines[split_idx+1:]))
        curr_idx = 0
        next_range = 1
        merged_ranges = [ranges[0]] 
        
        while next_range < len(ranges): 
            merged_range = merged_ranges[curr_idx]
            second_range = ranges[next_range]
            if second_range[0] <= merged_range[1]: 
                merged_range = (merged_range[0], max(second_range[1], merged_range[1])) 
                merged_ranges[curr_idx] = merged_range 
            else: 
                curr_idx += 1
                merged_ranges.append(second_range)
            next_range += 1
        
        fresh = 0
        
        print("Part one")
        for i in indexes: 
            for j in merged_ranges: 
                j = (j[0], j[1] + 1)
                if i in range(*j): 
                    fresh += 1
                    break
        print(fresh)
        
        numbers = 0        
        print("Part two")
        for j in merged_ranges: 
            numbers += j[1] - j[0] + 1
            
            
        print(numbers)
        
        
        
        
        
        
        
        
        


            

main() 

