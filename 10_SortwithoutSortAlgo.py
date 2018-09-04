def sort_scores(scores,highest_score):
    repository = [0] * (highest_score + 1)
    sorted_score = []
    
    for score in scores:
        repository[score] +=1
    
    for i in range(highest_score,-1,-1):
        count = repository[i]
        
        for j in range(count):
            sorted_score.append(i)
    
    return sorted_score
    
print(sort_scores([37, 89, 41, 65, 91, 53,91], 100))