def part_array(numbers, start, end):
    final_list =[]
    append = False
    
    for num in numbers:
        if num == start:
            append = True
        elif num == end:
            append = False
        if append:
            final_list.append(num)
    return final_list
    

numbers=[1,2,3,4,5,6,7,2]
print(part_array(numbers,4,7))

#Time complexity - O(n)
#Space complexity - O(n)