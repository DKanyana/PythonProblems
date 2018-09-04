import random

def pull_deck():
    deck = list(range(1,53))
    limit = 5
    pulls_list =[]
    
    while limit >0:
        next_pull = random.randint(0,len(deck)-1)
        pulls_list.append(deck[next_pull])
        del deck[next_pull]
        limit -= 1
    return pulls_list
        
    
print(pull_deck())