def isanagram(str1,str2):
    alpha_list = [0]*26
    offset = ord('a')
    sumOfch = 0
    
    for ch in str1:
        if ch.isalpha():
            alpha_list[ord(ch.lower())-offset] +=1
            
    for ch in str2:
        if ch.isalpha():
            alpha_list[ord(ch.lower())-offset] -=1
            
    for num in alpha_list:
        sumOfch +=num
    
    return sumOfch==0
    
str1 = 'the Morse.. code'
str2 = 'Here come.. dots'
print(isanagram(str1,str2))

#Time complexity - O(n)
#Space complexity - O(n)