def first_letter(sentence):
    first_list = []
    first_list.append(sentence[0])
    append_flag = False
    
    for ch in sentence:
        if append_flag:
            first_list.append(ch)
            append_flag = False
        if ch == ' ':
            append_flag = True
    return first_list
    
sentence = 'she sells sea shells in a sea shore'
print(first_letter(sentence))

#intialise a list
#add 1st char
#check for space and flag, append next of flag