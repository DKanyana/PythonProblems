def median_list(numbers):
    median = 0
    len_nums = len(numbers)
        
    if len_nums < 3:
        return 0
    else:
        midpoint =  len_nums//2 
        if len_nums%2 !=0:
            median = numbers[midpoint]
        else:
            median = (float(numbers[midpoint-1])+numbers[midpoint])/2
    return median
    
numbers = [1, 2, 12, 13, 15, 17, 26, 30, 38, 45]
print(median_list(numbers))

#Time complexity - O(1)
#Space complexity - O(1)

#sort the array
#find length
#find midpoint