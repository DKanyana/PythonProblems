# Python program to find largest, smallest, 
# second largest and second smallest in a
# list with complexity O(n)
def RangeList(list1):
    largest = list1[0]
    largest2 = list1[0]
    lowest = list1[0]
    lowest2 = list1[0]
    for item in list1:       
        if item > largest: 
            largest = item
        elif largest2!=largest and largest2 < item:
                largest2 = item
        elif item < lowest:
            lowest = item
        elif lowest2 != lowest and lowest2 > item:
            lowest2 = item
             
    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)
 
list1 = [12, 42, 2, 41, 31, 10, 8, 6, 4]
RangeList(list1)