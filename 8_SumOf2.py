def sumOf2(numbers,target):
    lookup = {}
    
    for cnt,num in enumerate(numbers):
        if target-num not in lookup:
            lookup[num] = cnt
        else:
            return (cnt,lookup[target-num])
    
numbers = [1,3,4,2,4,1,8]
target = 9
print(sumOf2(numbers,target))


#Lookup
#store num as key & index as val

#Time complexity - O(n)
#Space complexity - O(1)