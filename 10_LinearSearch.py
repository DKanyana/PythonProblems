def linearsearch(nums,target):
    
    for num in nums:
        if num==target:
            return True
    return False   
    
nums = [1,3,1,2,6,79,10]
print(binarysearch(nums,10))

#sort the array
#find midpoint, left <= right
#if target less equal than midpoint move left, else right
#Time Complexity - O(n)
#Space Complexity - O(1)