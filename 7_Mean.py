def mean_list(numbers):
    mean = 0
    count =0
    total = 0
    for num in numbers:
        total +=num
        count +=1
    mean = float(total)/count
    
    return mean
    
numbers = [1,3,5,2,5]
print(mean_list(numbers))

#Time complexity - O(n)
#Space complexity - O(1)