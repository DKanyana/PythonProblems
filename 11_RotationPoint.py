def rotation_point(words):
    firstword = words[0]
    left = 0
    right = len(words)-1
    
    while left < right:
        midpoint = (left + right)//2
        
        if words[midpoint] >= firstword:
            left = midpoint
        else:
            right = midpoint
            
        if left + 1 == right:
            if words[right]>=firstword:
                return 0
            else:
                return right
        return -1
    
print(find_rotation_point(['babka', 'banoffee', 'engender','karpatka', 'othellolagkage','asasd']))    
        