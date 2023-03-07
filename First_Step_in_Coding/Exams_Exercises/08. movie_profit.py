name_of_movie = input()
days = int(input())
tickets = int(input())
tickets_price = float(input())
percent_for_the_cinema = int(input()) / 100

price_of_tickets_per_day = tickets * tickets_price
revenue_for_the_entire_period = days * price_of_tickets_per_day
money_for_the_cinema = revenue_for_the_entire_period * percent_for_the_cinema
revenue_of_movie = revenue_for_the_entire_period - money_for_the_cinema

print(f"The profit from the movie {name_of_movie} is {revenue_of_movie:.2f} lv.")
