def missing_sum(nums):
    actual = 0
    expected = 0
    
    for num in nums:
        actual += num

    n = len(nums)+1
    expected = (n*n)/2
        
    return expected - actual
    
nums = [1,2,4,5,6]
print(missing_xor(nums))