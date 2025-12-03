import time

def recursive_split(start_str): 
    
    if(len(start_str) <= 2): return start_str
    
    side1 = recursive_split(start_str[:len(start_str) // 2])
    side2 = recursive_split(start_str[len(start_str) // 2:])
    
    l1 = None;l2 = None 
    
    for i in side1: 
        if l1 is None or i > l1: 
            l1 = i 
    
    for i in side2: 
        if l2 is None or i > l2: 
            l2 = i
            
    possible_largest = f"{l1}{l2}"
    
    if possible_largest < side1: 
         possible_largest = side1

    if possible_largest < side2: 
        possible_largest = side2

    return possible_largest 

accelerator_map = dict() 

# solved by combinatorics -- bleh 
def recursive_comb(digits, i, dig_num, static_dig_num): 
    global accelerator_map
    result = None 
    
    if i == len(digits) and dig_num > 0: 
        return - 10**20
    elif i == len(digits): 
        return 0

    number = None 
    an_number = None
    formatted_key = None
    
    formatted_key = f"{i}-{dig_num}"
    if formatted_key not in accelerator_map: 
        number = int(digits[i]) * 10**(dig_num - 1) + recursive_comb(digits, i + 1,  dig_num - 1, static_dig_num)
        accelerator_map[formatted_key] = number
    else: number = accelerator_map[formatted_key]
    
    formatted_key = f"W-{i}-{dig_num}"
    if formatted_key not in accelerator_map: 
        an_number = recursive_comb(digits, i + 1, dig_num, static_dig_num)
        accelerator_map[formatted_key] = an_number
    else: an_number = accelerator_map[formatted_key]
    
    result = an_number
    result = max(result, int(number))
    
    return result 

def main():
    global accelerator_map
    with open("./test.txt", "r") as file: 
        lines = file.read().splitlines()  
        result = 0
        start = time.perf_counter() 
        for line in lines: 
            # part 1 
            #result += int(recursive_split(line))
            # part 2 
            #print(max)
            accelerator_map = dict()            
            return_val = recursive_comb(line, 0, dig_num=12, static_dig_num=12)
            result += return_val
        end = time.perf_counter() 
        print(f"elapsed time: {(end - start):.6f} seconds")
        print(result)
        #167523425665348 correct
    pass

main() 
