import re
import math

def main(): 
    
    with open("./test.txt", "r") as file:
        
        content = re.sub(r"\n", "", file.read())  
        ranges = content.split(",")
        
        for i in range(len(ranges)): 
            ranges[i] = ranges[i].split("-")

        result = 0
        for i in ranges:
            item1 = i[0]
            item2 = i[1]
            for j in range(int(item1), int(item2) + 1):
                str_i = str(j)
                is_pattern = False
                for divider in range(2, len(str_i) + 1): 
                    if len(str_i) % divider != 0: continue 
                    is_pattern = True
                    checkpoint = len(str_i) // divider 
                    first_one = str_i[:checkpoint]
                    for i in range(checkpoint, len(str_i), checkpoint): 
                        if str_i[i:i + checkpoint] != first_one: 
                            is_pattern = False
                            continue 
                    if is_pattern: 
                        break 
                if is_pattern: 
                    print(j)
                    result += j
        print(result)        

main() 