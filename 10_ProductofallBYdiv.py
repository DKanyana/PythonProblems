def get_products_of_all_ints_except_at_index_bydiv(nums):
    productofall = 1
  
    for num in nums:
        productofall *= num

    for i in range(len(nums)):
        nums[i]= int(productofall/nums[i])
   
    return nums
    
    
nums = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index_bydiv(nums))