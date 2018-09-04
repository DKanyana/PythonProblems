def permutation_palindrome(word):
    unpaired_char = set()
    
    for char in word:
        if char not in unpaired_char:
            unpaired_char.add(char)
        else:
            unpaired_char.remove(char)
    
    return len(unpaired_char)<=1
    
print(permutation_palindrome('cicvi'))