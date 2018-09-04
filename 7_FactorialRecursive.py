def recursive_fact(num):
    if num ==0:
        return 0
    else:
        return num * recursive_fact(num-1)
num = 4
print(factorial(num))