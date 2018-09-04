def armstrong_num(num):
    original_number = num
    armstrong = 0
    digit_count = 0
    digit = []
    
    while num > 0:
        digit.append(num%10)
        num = num//10
        digit_count +=1
    for i in digit:
        armstrong = armstrong + i**digit_count
    
    return armstrong == original_number
    
num = 9474
print(armstrong_num(num))

#copy num
#mod and divide to get all digits
#count number of digits
