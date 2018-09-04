def find_repeat(numbers_list):
    n = len(numbers_list) - 1
    sumoflist = 0
    
    for num in numbers_list:
        sumoflist += num
        
    triangularseries_sum = int(((n+1)*n)/2)
    
    return sumoflist-triangularseries_sum
    
    

print(find_repeat([4, 1, 3, 4, 2]))