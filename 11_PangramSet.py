import string
def ispangram(str1):
    alphaset = set(string.ascii_lowercase)
    return set(str1)>=alphaset
    
    
str1 = 'The quick brown fox jumps over the lazy dog'
print(ispangram(str1))