import math
def prime_factors(num):
    n = num
    pf =[]
    
    while num%2 == 0:
        pf.append(2)
        num =num/2
    
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while num%i == 0:
            pf.append(i)
            num = num/i

    return pf
    
num = 60
print(prime_factors(num))

#Check if the number is divisible by 2
#Check from 3 to sqrt of number