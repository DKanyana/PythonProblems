def startwiths(sentence):
    sen_list =sentence.strip().split()
    s_list = []
    
    for word in sen_list:
        if word[0].lower() =='s':
            s_list.append(word)
    return s_list
    
sentence = 'she Sells sea shells in sea shore'
print(startwiths(sentence))

#intialise a list
#split into list
#check start letter
