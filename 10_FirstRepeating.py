def first_repeating(nums):
    seen_dict ={}
    
    for num in nums:
        if num not in seen_dict:
            seen_dict[num] = True
        else:
            return num
    
    
    
nums = [1,2,3,2,4,5]
print(first_repeating(nums))