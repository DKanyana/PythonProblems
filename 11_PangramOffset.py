def ispangram(str1):
    alphabet_list = [0]*26
    offset = ord('a')
    
    for ch in str1.lower():
        if ch.isalpha():
            alphabet_list[ord(ch)-offset] +=1
            
    for num in alphabet_list:
        if num == 0:
            return False
    
    return True
            
    
    
str1 = 'The quick brown fox jumps over the lazy dog'
print(ispangram(str1))