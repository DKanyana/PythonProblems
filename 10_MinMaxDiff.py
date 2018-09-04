def minmax_diff(nums):
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
        elif num >max_num:
            max_num = num
            
    return max_num - min_num

nums = [1,3,1,2,6,79,10]
print(minmax_diff(nums))