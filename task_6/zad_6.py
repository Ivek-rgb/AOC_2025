import re 
from copy import deepcopy

def main(): 
    
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
        
        operators = [  operator for operator in  lines[len(lines) - 1].split(' ') if operator != '']
        numbers = lines[:len(lines) - 1]
        
        print(operators)
        
        max_len = None
        
        for i in range(len(numbers)): 
            patterns = list(map(lambda x: len(x),re.findall(r"\d+", numbers[i])))
            if not max_len:
                max_len = [0] * len(patterns)
            for j in range(len(patterns)):
                max_len[j] = max(max_len[j], patterns[j])

        extracted_numbers = [None] * len(numbers)
        pos_sum = 0
        
        result = 0
        
        for i in range(len(max_len)): 
            extracted_numbers = [] 
            for j in range(len(numbers)): 
                position_idx = pos_sum + i * 1 
                extracted_numbers.append((numbers[j][position_idx:position_idx + max_len[i]]))
            pos_sum += max_len[i]
            
            result_num = ''
            result_save = 0 

            operation = (lambda x, y: x * y) if operators[i] == '*' else (lambda x, y: x + y) 
            
            for k in range(max_len[i]): 
                result_num = ''
                for l in range(len(numbers)): 
                    digit = extracted_numbers[l][k] 
                    result_num += digit if digit != ' ' else ''
                print(result_num)
                if k > 0: 
                    result_save = operation(result_save, int(result_num))
                else:
                    result_save = int(result_num)
            print(f"partial result: {result_save}") 
            result += result_save    
        print(result)

main() 