def lcm(num1,num2):
    greater = 0
    
    if num1 > num2:
        greater = num1
    elif num2 > num1:
        greater = num2
        
    while True:
        if greater%num1 ==0 and greater%num2==0:
            break
        greater +=1
    return greater
num1 = 54 
num2 = 24
print(lcm(num1,num2))

#Find the greatest number
#keep incrementing greater
# greater must divide both numbers