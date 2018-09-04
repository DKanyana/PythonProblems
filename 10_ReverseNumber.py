def reverse_num(num):
    revnum = 0
    
    while num > 0:
        revnum = revnum*10 + (num%10)
        num = num//10
    
    return revnum
    
num = 496
print(reverse_num(num))

#mod num by 10 and divide by 10
#count till num>0
