def binarysearch(nums,target):
    sorted_nums = sorted(nums)
    left_index = 0
    right_index = len(sorted_nums)-1
    found = False
    
    while left_index <= right_index and not found:
        midpoint = (left_index+right_index)//2
        if target == sorted_nums[midpoint]:
            found = True
        else:
            if target < sorted_nums[midpoint]:
                right_index = midpoint-1
            else:
                left_index = midpoint +1
    return found   
    
nums = [1,3,1,2,6,79,10]
print(binarysearch(nums,78))

#sort the array
#find midpoint, left <= right
#if target less equal than midpoint move left, else right
#Time Complexity - O(lg n)
#Space Complexity - O(1)