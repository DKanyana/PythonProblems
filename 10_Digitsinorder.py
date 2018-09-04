def digits(num):
    count_digits = 0
    digits = []
    
    while num > 0:
        digits.append(num%10)
        num = num//10
        count_digits +=1
    
    left_index = 0
    right_index = count_digits -1
    
    while left_index < right_index:
        digits[left_index],digits[right_index] = digits[right_index],digits[left_index]
        left_index +=1
        right_index -=1
    
    return digits
    
num = 496
print(digits(num))

#mod num by 10 and divide by 10
#count till num>0
