def zipmax_tups(num1,num2):
    num1_index = 0
    num2_index = 0
    max_len = max(len(num1),len(num2))
    zip_index = 0
    zip_list =[]
    tup1 = 0
    tup2 = 0

    while zip_index < max_len:
        isnum1_empty = num1_index >=len(num1)
        isnum2_empty = num2_index >=len(num2)
        
        if isnum1_empty:
            tup1 = 0
            tup2 = num2[num2_index]
        elif isnum2_empty:
            tup1 = num1[num1_index]
            tup2 = 0
        else:
            tup1 = num1[num1_index]
            tup2 = num2[num2_index]
            
        zip_list.append((tup1,tup2))
        num1_index +=1
        num2_index +=1
        zip_index +=1
    
    return zip_list
                          
num1=[1,3,5,7,9]
num2=[2,4,6,8,10,12]
print(zipmax_tups(num1,num2))

#create final list with len of min list
# have 3 index - num1,num2,final
#zip each pair and increament till final ends