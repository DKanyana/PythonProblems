import random

def shuffle_list(nums):
    endoflist = len(nums)
    for i in range(endoflist-1):
        random_index = random.randrange(i+1,endoflist)
        nums[i],nums[random_index] = nums[random_index], nums[i]
    return nums
        
    
print(shuffle_list([1, 2, 3, 4, 5]))