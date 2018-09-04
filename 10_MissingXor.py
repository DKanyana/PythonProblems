def missing_xor(nums):
    actual = 0
    expected = 0
    
    for num in nums:
        actual ^= num

    for i in range(1,len(nums)+2):
        expected ^=i
        
    return actual ^ expected
    
nums = [1,3,4,5,6]
print(missing_xor(nums))

#xor of array elements
#xor of all elements from 1 till len+1
# xor of above 2