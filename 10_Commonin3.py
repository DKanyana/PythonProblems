def common_in_3Array(arr1,arr2,arr3):
    i,j,k = 0,0,0
    common =[]
    while i<len(num1) and j<len(num2) and k<len(num3):
        if (arr1[i]==arr2[j] and arr2[j]==arr3[k]):
            common.append(arr1[i])
            i +=1
            j +=1
            k +=1
        elif arr1[i]<arr2[j]:
            i +=1
        elif arr2[j]<arr3[k]:
            j +=1
        else:
            k +=1
    
    return common
num1 =[2,4,6,7]
num2 =[1,2,4,5,6]
num3 =[4,5,6]

print(common_in_3Array(num1,num2,num3))

#Loop runs till one array ends
#if all elements are same, all index increment
#else only specific index increments