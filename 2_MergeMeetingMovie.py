def merge_meeting(movies):
    total_time = 0
    sorted_movies = sorted(movies)
    merge_movie = [sorted_movies[0]]
    
    for curr_start,curr_end in sorted_movies[1:]:
        prev_start, prev_end = merge_movie[-1]
        
        if curr_start < prev_end:
            merge_movie[-1] = (prev_start,max(curr_end, prev_end))
        else:
            merge_movie.append((curr_start, curr_end))
    print(sorted_movies)
    print(merge_movie)
    
    for start,end in merge_movie:
        total_time +=end -start
        
    return total_time
movies = [(0,5),(6,10),(8,9),(2,4)]
print(merge_meeting(movies))

#sort - initial time
#overlap or not 
#overlap - next meeting start less than prev meeting end. max end time
#not overlap - next meeting start is greater than prev meeting. end !
#Time complexity - O(n)
#Space complexity - O(n)