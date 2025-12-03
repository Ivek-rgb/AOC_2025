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
def recursive_comb(digits, dig_num, static_dig_num): 
    global accelerator_map
    result = None 
    
    if len(digits) == 1: return digits[0]

    number = None 
    an_number = None
    formatted_key = None

    for i in range(len(digits) - 1):
        
        if(len(digits) - i + static_dig_num - dig_num  < static_dig_num): break
        
        formatted_key_non = f"{digits[i]}-{dig_num}-{digits[i+1:]}"
        if formatted_key_non not in accelerator_map: 
            number = digits[i] + (recursive_comb(digits[i+1:], dig_num - 1, static_dig_num) if dig_num - 1 > 0 else "")
            accelerator_map[formatted_key_non] = number
        else: number = accelerator_map[formatted_key_non]

        formatted_key_skip = f"W-{dig_num}-{digits[i+1:]}"
        if formatted_key_skip not in accelerator_map: 
            an_number = recursive_comb(digits[i+1:], dig_num, static_dig_num)
            accelerator_map[formatted_key_skip] = an_number
        else: an_number = accelerator_map[formatted_key_skip]
        if an_number is None or int(number) > int(an_number): 
            larger = number
        else: 
            larger = an_number
        
        if larger != None and (result is None or int(result) < int(larger)): 
            result = larger
    
    return result 

def snd_main(): 
    print(recursive_comb("987654321111111987654321111111987654321111111987654321111111", dig_num=12, static_dig_num=12)) 

#snd_main() 

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
            max = None
            #print(max)
            return_val = recursive_comb(line, dig_num=12, static_dig_num=12)
            result += int(return_val)
        end = time.perf_counter() 
        print(f"elapsed time: {(end - start):.6f} seconds")
        print(result)
        #167523425665348
    pass

main() 
