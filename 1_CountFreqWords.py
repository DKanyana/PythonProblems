import string
def frequency_words(sentence):
    word_hash = {}
    
    #Remove punctuation, trim and lowercase
    punctuation_set = set(string.punctuation)
    temp_list = []
    for char in sentence.strip().lower():
        if char not in punctuation_set:
            temp_list.append(char)
    words_withoutpunctuation = ''.join(temp_list)
    
    temp_list = words_withoutpunctuation.split()
    for word in temp_list:
        if word not in word_hash:
            word_hash[word] = 1
        else:
            word_hash[word] += 1
    return  word_hash
    
    
sentence = 'My name is, Mishika Paul Singh My my'
print(frequency_words(sentence))

#split sentence words
#lowercase
#strip space 
#Time complexity - O(n)
#Space complexity - O(n)
