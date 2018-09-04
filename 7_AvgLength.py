def avg_length(sentence):
    len_sentence = 0
    noofwords =0
    
    for char in sentence.strip():
        if char !=' ' and char.isalpha():
            len_sentence +=1
        elif char == ' ':
            noofwords +=1
    print(len_sentence)
    print(noofwords)
    
    return float(len_sentence)/(noofwords+1)
    
sentence ='my name is deeksha'
print(avg_length(sentence))

#strip spaces
#length of sentence excluding spaces
#no of words