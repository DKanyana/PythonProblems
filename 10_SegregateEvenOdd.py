def segregate_evenodd(nums):
    left = 0
    right = len(nums)-1
    
    while left <right:
        while nums[left]%2 ==0 and left<right:
            left +=1
        while nums[right]%2 ==1 and left<right:
            right -=1
        if left <right:
            nums[left], nums[right] = nums[right],nums[left]
            left +=1
            right -=1
    return nums
    
nums = [13,1,3,4,2,11,5,8,9,6]
print(segregate_evenodd(nums))