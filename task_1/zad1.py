start = 50 

def main(): 
    global start
    counter = 0 
    with open("./test.txt", "r") as file:
        save_state = None 
        for i in file.readlines(): 
            line = i.split("\n")[0]
            arr, val = line[0], line[1:]
            save_state = start 
            val = int(val)
            start += (val % 100) * (-1 if arr == "L" else 1)
            counter += int(val / 100)
            if save_state * start < 0:  
                counter += 1  
            if start / 100 > 1 or start % 100 == 0: 
                counter += 1
            start %= 100 
            print(f"{start} counter: {counter}")
        print(counter)
                    
main() 

