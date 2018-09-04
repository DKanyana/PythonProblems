def fibonacci(num):
    fib =[0,1]
    
    if num <2:
        return fib
    else:
        for i in range(2,num):
            fib.append(fib[i-1]+fib[i-2])
    return fib
    
num = 9
print(fibonacci(num))

#copy num
#mod and divide to get all digits
#count number of digits