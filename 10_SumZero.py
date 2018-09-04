def sum_zero(nums):
    lookup = {}
    target = 0
    
    for cnt,val in enumerate(nums):
        if target - val in lookup:
            return True
        else:
            lookup[val] = cnt
    return False

nums = [6,-1,2,8,-9]
print(sum_zero(nums))