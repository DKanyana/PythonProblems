def thrice_char(sentence):
    char_list = []
    for char in sentence:
        char_list.append(char*3)
    
    return ''.join(char_list)
    
sentence = 'hello hji'
print(thrice_char(sentence))