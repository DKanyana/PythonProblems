def poker(num1,num2,num3):
    sumofnums = num1 + num2 + num3
    
    if sumofnums > 21 and (num1==11 or num2==11 or num3==11):
        sumofnums -=10
        
    if sumofnums > 21:
        return 'BUST'
    else:
        return sumofnums
num1,num2,num3 = 11, 10,11
print(poker(num1,num2,num3))

# Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'