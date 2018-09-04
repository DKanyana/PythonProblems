#Write a function that takes an integer flight_length (in minutes) 
#and a list of integers movie_lengths (in minutes) and returns a 
#boolean indicating whether 
#there are two numbers in movie_lengths whose sum equals flight_length.

def can_two_movies_fill_flight(movie_lengths, flight_length):
    movies_seen = set()
    
    for firstmovielength in movie_lengths:
        if flight_length - firstmovielength in movies_seen:
            return True
        else:
            movies_seen.add(firstmovielength)
    
    return False
    
print(can_two_movies_fill_flight([100,40,150,76,80,210],300))