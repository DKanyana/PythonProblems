def get_products_of_all_ints_except_at_index(nums):
    product = [0] * len(nums)

    productsofar = 1
    for i in range(len(nums)):
        product[i]=productsofar
        productsofar *=nums[i]
    
    productsofar = 1
    for i in range(len(nums)-1,-1,-1):
        product[i] = product[i] * productsofar
        productsofar = productsofar * nums[i]
        
    return product
    
    
nums = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(nums))