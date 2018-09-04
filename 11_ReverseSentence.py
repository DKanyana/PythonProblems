def reverse_word(sentence,left,right):
    while left < right:
        sentence[left],sentence[right] = sentence[right],sentence[left]
        left +=1
        right -=1
    return sentence

def reverse_sentence(sentence):
    reverse_word(sentence,0,len(sentence)-1)
    startindex =0
    print(sentence)
    
    for i in range(len(sentence)+1):
        if i ==len(sentence) or sentence[i] == ' ' :
            reverse_word(sentence,startindex,i-1)
            startindex = i+1
    return sentence
    
sentence = 'deeksha is my name'
print(reverse_sentence(list(sentence)))