def merge_sortedlists(mylist,alicelist):
    merged_list = [0]*(len(mylist)+len(alicelist))
    mylist_index = 0
    alicelist_index = 0
    mergedlist_index =0
    
    while mergedlist_index < len(merged_list):
        ismylist_empty = mylist_index >=len(mylist)
        isalicelist_empty = alicelist_index >= len(alicelist)
        
        if not ismylist_empty and (mylist[mylist_index]<alicelist[alicelist_index] or isalicelist_empty) :
            merged_list[mergedlist_index] = mylist[mylist_index]
            mylist_index +=1
        else:
            merged_list[mergedlist_index] = alicelist[alicelist_index]
            alicelist_index +=1
        
        mergedlist_index +=1
        
    return merged_list
        
print(merge_sortedlists([2, 4, 6], [1, 3, 7]))