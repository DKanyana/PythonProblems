def count_word(sentence):
    word_count =0
    for ch in sentence:
        if ch==' ':
            word_count +=1 
    return (word_count+1)
    
sentence = 'My, name is Mishika Paul Singh.'
print(count_word(sentence))

# cnt = sentence.count(' ')
#Time Complexity = O(n)
#Space Complexity = O(1)