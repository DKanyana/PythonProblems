def reverseList(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left +=1
        right -=1
    return nums

nums = [13,1,3,4,2,11,5,8,9,6]
print(reverseList(nums))