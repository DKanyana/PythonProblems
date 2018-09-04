def perfect_number(num):
    sumofdivisors = 0
    
    for i in range(1,num):
        if num%i ==0:
            sumofdivisors += i
    return num==sumofdivisors
    
num = 496
print(perfect_number(num))

#from 1 to num-1, sum all the divisors
# check with the num