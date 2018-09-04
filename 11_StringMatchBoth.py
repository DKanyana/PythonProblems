def string_match_both(a, b):
    longer, shorter = a,a
    
    if len(a)>len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter =a

    count = 0

    for i in range(len(shorter)-1):
        sub=shorter[i:i+2]
        if sub in longer:
            print(sub)
            count +=1
      
    return count

print(string_match('xxacazz', 'xxbcaazi'))