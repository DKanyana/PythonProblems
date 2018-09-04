def make_tupes(numbers):
    tups_list= []
    start_index =0
    
    while start_index < len(numbers)-1:
        tups_list.append((numbers[start_index],numbers[start_index+1]))
        start_index = start_index+2
        
    return tups_list     
            
    
numbers = [1,3,4,2,4,1,8,9]
print(make_tupes(numbers))


#Lookup
#store num as key & index as val

#Time complexity - O(n)
#Space complexity - O(n)