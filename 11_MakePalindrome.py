#The minimum number of operations needed to make the string a palindrome.

def theLoveLetterMystery(s):
    left = 0
    right = len(s)-1
    noofops = 0
    
    while left < right:
        noofops += abs(ord(s[left]) - ord(s[right]))
        left +=1
        right -=1
        
    return noofops

print(theLoveLetterMystery('abcde'))
#Result = 6