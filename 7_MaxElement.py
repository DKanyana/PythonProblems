def max_element(numbers):
    max_e = 0
    for num in numbers:
        if num > max_e:
            max_e = num
    return max_e
    
numbers=[34,1,45,67,3]
print(max_element(numbers))

#Time complexity - O(n)
#Space complexity - O(1)