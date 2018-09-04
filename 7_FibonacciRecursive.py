def fibonacci_recursive(num):
    fib =[0,1]
    
    if num <2:
        return fib
    else:
        return fibonacci_recursive[num-1]+fibonacci_recursive[num-2]
    
num = 9
print(fibonacci(num))

#copy num
#mod and divide to get all digits
#count number of digits
