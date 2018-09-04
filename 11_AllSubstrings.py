def findsubstrings(word):
    substr = []
    ln_word = len(word)
    for i in range(ln_word):
        for j in range(i+1,ln_word+1):
            print(word[i:j])
            substr.append(word[i:j])
    
    return substr
        
print(findsubstrings('deeksha'))