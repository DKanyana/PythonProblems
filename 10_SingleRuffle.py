def is_single_riffle(half1, half2, shuffled_deck):
    half1_index = 0
    half2_index = 0
    
    for card in shuffled_deck:
        ishalf1_empty = half1_index >= len(half1)
        ishalf2_empty = half2_index >= len(half2)
        
        if not ishalf1_empty and half1[half1_index] == card:
            half1_index += 1
        elif not ishalf2_empty and half2[half2_index] == card:
            half2_index += 1
        else:
            return False
    return True
    
print(is_single_riffle([1, 5], [2, 3, 6], [1, 5, 6, 3, 2]))