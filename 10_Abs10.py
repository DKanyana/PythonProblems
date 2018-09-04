def abs_within10(num):
    if abs(num-100) <= 10 or abs(num-200) <= 10:
        return True
    
    return False
    
num = 1
print(abs_within10(num))