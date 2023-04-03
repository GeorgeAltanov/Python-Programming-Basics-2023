movies = int(input())

max_rating = float("-inf")
min_rating = float("inf")
min_rating_movie = None
max_rating_movie = None
average_rating = 0
counter = 0

while True:
    name_movies = input()
    rating = float(input())
    average_rating += rating
    if rating >= max_rating:
        max_rating = rating
        max_rating_movie = name_movies

    if rating < min_rating:
        min_rating = rating
        min_rating_movie = name_movies
    counter += 1

    if counter == movies:
        break
        
print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating / movies:.1f}")
