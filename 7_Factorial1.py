def factorial(num):
    factorial = 1
    if num ==0:
        return 0
    else:
        while num > 0:
            factorial = factorial * num 
            num = num-1
    return factorial
    
num = 4
print(factorial(num))