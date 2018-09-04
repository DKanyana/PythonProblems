def minabsdiff(nums):
    nums = sorted(nums)
    absdiff = abs(nums[1]-nums[0])
    
    for i in range(1,len(nums)):
        absdiffcur = abs(nums[i]-nums[i-1])
        absdiff = min(absdiff,absdiffcur)
    
    return absdiff

nums = [12, 42, 2, 41]
print(minabsdiff(nums))