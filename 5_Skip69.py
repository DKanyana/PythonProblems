def skip_69(numbers):
    total = 0
    add = True
    
    for num in numbers:
        if num!=6 and add:
            total +=num
        else:
            add = False
        if num == 9:
            add=True
    return total
    
numbers=[1,2,3,4,5,6,7,2,4,7,9,16,8,9]
print(skip_69(numbers))

#Time complexity - O(n)
#Space complexity - O(1)