def make_bricks(small, big, goal):
    if goal > (big*5 + small):
        return False
    elif goal%5 > small:
            return False
        
    return True
    
print(make_bricks(6, 2, 7))