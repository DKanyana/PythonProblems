def first_nonrecurr(nums):
    nums_seen = []
    
    for num in nums:
        if num not in nums_seen:
            nums_seen.append(num)
        else:
            nums_seen.remove(num)
    return nums_seen[0]
    
    
nums = [1,2,3,4,2,3,4,5,1]
print(first_nonrecurr(nums))