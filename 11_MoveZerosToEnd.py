def move_zerostoend(nums):
    left =0 
    right = len(nums)-1
    
    while left < right:
        while nums[left]!=0 and left<right:
            left +=1
        while nums[right]==0 and left<right:
            right -=1
            
        if left < right:
            nums[left],nums[right]=nums[right],nums[left]
            left +=1
            right -=1
    return nums
        
    
nums = [1,0,0,2,3,0,4,5]
print(move_zerostoend(nums))