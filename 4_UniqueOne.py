def find_one_uniq(numbers):
    uniq =0 
    for num in numbers:
        uniq ^= num
    return uniq
    
numbers= [1,2,2,3,3,4,4,5,5,1,7]
print(find_one_uniq(numbers))

#Time complexity - O(n)
#Space complexity - O(1)