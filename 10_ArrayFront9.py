#Given an array of ints, return True if one of the first 4 elements 
#in the array is a 9. The array length may be less than 4.

def array_front9(nums):
    limit = 4
    if len(nums) < 4:
        limit =len(nums)

    for i in range(limit):
        if nums[i] == 9:
            return True
    return False

num=[1,2,9,4,5,7]
print(array_front9(num))
