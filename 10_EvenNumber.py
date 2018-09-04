def even_nums(nums):
    even_list = []
    
    for num in nums:
        if num%2 ==0:
            even_list.append(num)
    return even_list
    
nums = [2,3,6,66,2,4,7,8]
print(even_nums(nums))


