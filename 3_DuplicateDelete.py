#Soln 1--- delete duplicates 
#Time complexity - O(n)
#Space complexity - O(n)
def delete_duplicate(dup_list):
    dup_dict ={}
    i=0
    
    while i<len(dup_list):
        if dup_list[i] not in dup_dict:
            dup_dict[dup_list[i]] = True
            i +=1
        else:
            dup_list.pop(i)
    return dup_list
  
dup_list = [1,1,2,2,3,3,5,5,5]
print(delete_duplicate(dup_list))

#Soln 2 ---
#Time complexity - O(n)
#Space complexity - O(n)
def delete_duplicate(dup_list):
    uniq_set = set(dup_list)
    return (list(uniq_set))
dup_list = [1,1,2,2,3,3,5,5,5]
print(delete_duplicate(dup_list))

#initial set to store unique
#if not present, add to set
#else remove from list
#dup will be unique list
#a=[1,2,3]
#a.remove(2)
# a
#[1, 3]
# a=[1,2,3]
#del a[1]
# a
#[1, 3]
# a= [1,2,3]
# a.pop(1)
#2
# a
#[1, 3]
# 