max_points = 0
winner_movie = None
counter_movie = 0

while True:
    movie = input()
    counter_movie += 1
    total_points = 0

    if movie == "STOP":
        break
    length_of_symbol_movie = len(movie)

    for symbol in movie:
        points = ord(symbol)

        if 65 <= ord(symbol) <= 90:
            points -= length_of_symbol_movie

        elif 97 <= ord(symbol) <= 122:
            points -= 2 * length_of_symbol_movie

        total_points += points

        if total_points >= max_points:
            max_points = total_points
            winner_movie = movie

    if counter_movie >= 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {winner_movie} with {max_points} ASCII sum.")
