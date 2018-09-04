def palidrome_withlist(word):
    char_list = []

    for ch in word:
        if ch.isalpha():
            char_list.append(ch)
    
    left_index = 0
    right_index = len(char_list)-1

    while left_index < right_index:    
        if char_list[left_index].lower() == char_list[right_index].lower():
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
#Space complexity - O(n)