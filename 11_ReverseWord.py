def reverse_string(word):
    charlist = list(word)
    left = 0
    right = len(charlist)-1
    print(charlist)
    
    while left < right:
        charlist[left],charlist[right] = charlist[right],charlist[left]
        left +=1
        right -=1
    return ''.join(charlist)

word = 'deeksha'
print(reverse_string(word))