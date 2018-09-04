def gcd_hcf(num1,num2):
    small = 0
    gcd = 1
    
    if num1 < num2:
        small = num1
    elif num2< num1:
        small = num2
        
    for i in range(1,small+1):
        if num1%i ==0 and num2%i==0:
            gcd = i
        
    return gcd
num1 = 36 
num2 = 60
print(gcd_hcf(num1,num2))

# loop from 1 to smallest number (small+1)
# the greatest number that divides both numbers in gcd or hcf