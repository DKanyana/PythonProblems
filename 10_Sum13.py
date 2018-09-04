def sum13(nums):
  if len(nums)<0:
    return 0
    
  sum13 = 0
  index = 0
    
  while index < len(nums):
    if nums[index]==13:
      index +=2
    else:
      sum13 +=nums[index]
      index +=1
    return sum13
    
print(sum13([2,3,4,5,13,4,3,13]))

#Return the sum of the numbers in the array, returning 0 for an 
#empty array. Except the number 13 is very unlucky, so it does not 
#count and numbers that come immediately after a 13 also do not count.