def unique_words(sentence):
    unique_word_count= 0
    word_list = sentence.lower().strip().split()
    #unique_set = set(word_list)
    hash_wordmap = {}
    for word in word_list:
        if word not in hash_wordmap:
            hash_wordmap[word] = True
    return len(hash_wordmap)
    
sentence = 'My name is Mishika Paul Singh My my'
print(unique_words(sentence))

#Time Complexity = O(n)
#Space Complexity = O(n)