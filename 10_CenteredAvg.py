def centered_avg(nums):
    min_num = nums[0]
    max_num = nums[0]
    sumofnums = 0
    centered_avg = 0
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
        sumofnums +=num
    print([sumofnums,max_num,min_num])
    centered_avg = (sumofnums-max_num-min_num)/(len(nums)-2)

    return centered_avg
    
nums = [1,2,3,4,5]
print(centered_avg(nums))