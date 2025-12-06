import re 
from copy import deepcopy
import time

def main(): 
    
    start = time.perf_counter() 
    with open("./test.txt", "r") as file: 
        lines = file.read().splitlines() 
        
        #for idx in range(len(lines)):
            #lines[idx] = re.split(r'\s+', lines[idx])
            #lines[idx] = [x for x in lines[idx] if x != ''] 
        
        """
        ## PART ONE ##  
        
        result = 0
        for idx in range(len(lines[0])):
            mid_result = int(lines[0][idx])
            operation = (lambda x, y: x * y) if lines[len(lines) - 1][idx] == '*' else (lambda x, y: x + y) 
            for j in range(1, len(lines) - 1):
                mid_result = operation(mid_result, int(lines[j][idx]))
            print(mid_result)
            result += mid_result
        """            
        
        # Part two 
        # can also be done much more statically with this operator lengths but yeah, you can also do one with regex iterator 
        operators = lines[len(lines) - 1]
        operator_lens = list(map(lambda x: len(x) - 1, re.findall(r"[+*]\s+", operators)))   
        operator_lens[len(operator_lens) - 1] += 1     
                
        operators = [operator for operator in  operators.split(' ') if operator != '']
        numbers = lines[:len(lines) - 1]

        extracted_numbers = []
        pos_sum = 0
        result = 0
        
        for i in range(len(operator_lens)):
            extracted_numbers = [] 
            for j in range(len(numbers)): 
                position_idx = pos_sum + i * 1
                extracted_numbers.append(numbers[j][position_idx:position_idx + operator_lens[i]]) 
            pos_sum += operator_lens[i]
            
            result_num = ''
            result_save = 0 
            for k in range(operator_lens[i]): 
                result_num = ''
                for l in range(len(numbers)): 
                    digit = extracted_numbers[l][k] 
                    result_num += digit if digit != ' ' else ''
                if k > 0: 
                    if operators[i] == '*':
                        result_save *= int(result_num)
                    else:
                        result_save += int(result_num)
                else:
                    result_save = int(result_num)
            result += result_save    
        print(result)
    end = time.perf_counter() 
    print(f"elapsed time {(end-start):.6f} seconds")
    
    
main() 