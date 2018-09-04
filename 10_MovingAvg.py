def moving_avg(nums):
    movingavg = []
    sumofnums = 0
    countofnums =0
    
    for num in nums:
        
        sumofnums += num
        countofnums +=1
        movingavg.append(float(sumofnums)/countofnums)

    return movingavg
    
nums = [1,2,3,4,5]
print(moving_avg(nums))