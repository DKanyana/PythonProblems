def palidrome_inplace(word):
    left_index = 0
    right_index = len(word)-1

    while left_index < right_index:
        while not word[left_index].isalpha() and left_index < right_index:
            left_index +=1
        while not word[right_index].isalpha() and left_index < right_index:
            right_index -=1
            
        if word[left_index].lower() == word[right_index].lower():
            left_index +=1
            right_index -=1
        else:
            return False
    return True

word = 'May a moody baby doom a yam?'
print(palidrome(word))

#strip spaces
#lowercase comparison
#ignore spaces

#Time complexity - O(n)
#Space complexity - O(1)