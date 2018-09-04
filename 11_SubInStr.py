def substr_instr(str1,sub):
    count =0
    sub_len = len(sub)
    str1_len = len(str1)
    
    if sub_len > str1_len:
        return 0
    
    for i in range(str1_len - sub_len+1):
        if str1[i:i+sub_len]==sub:
            count +=1
    
    
    return count
    
str1 = 'xxacabzzcaxccabb'
sub = 'cab'
print(substr_instr(str1,sub))