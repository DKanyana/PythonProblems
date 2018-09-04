def zip_tups(num1,num2):
    num1_index = 0
    num2_index = 0
    min_len = min(len(num1),len(num2))
    zip_index = 0
    zip_list =[]

    while zip_index < min_len:
        zip_list.append((num1[num1_index],num2[num2_index]))
        num1_index +=1
        num2_index +=1
        zip_index +=1
    
    return zip_list
                          
num1=[1,3,5,7,9]
num2=[2,4,6]
print(zip_tups(num1,num2))

#create final list with len of min list
# have 3 index - num1,num2,final
#zip each pair and increament till final ends