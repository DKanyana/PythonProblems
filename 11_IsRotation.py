def is_rotation(str1,str2):
    double_str2 = str2*2
    if str1 in double_str2:
        return True
    return False
    
str1 = 'eye'
str2 = 'yee'
print(is_rotation(str1,str2))