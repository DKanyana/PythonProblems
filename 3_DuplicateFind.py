def find_duplicates(duplicates):
    duplist = []
    dup_dict = {}
    
    for num in duplicates:
        if num not in dup_dict:
            dup_dict[num] = 1
        else:
            dup_dict[num] +=1
    
    for key, val in dup_dict.items():
        if val >1:
            duplist.append(key)
    
    return duplist
    
def find_duplicates_1(duplicates):
    duplist = set()
    num_seen = set()
    for num in duplicates:
        if num not in num_seen:
            num_seen.add(num)
        else:
            duplist.add(num)
    return list(duplist)

duplicates = [1,2,3,3,2,4523,56,1,2,6,5,6]
print(find_duplicates(duplicates))
print(find_duplicates_1(duplicates))

#Time complexity -O(n)
#Space complexity -O(n)

