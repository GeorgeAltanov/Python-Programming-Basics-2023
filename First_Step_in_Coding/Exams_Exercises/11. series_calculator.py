from math import ceil

name_of_movie = input()
seasons = int(input())
episodes = int(input())
time_of_episode_without_advertisement = float(input())

time_of_advertisement = time_of_episode_without_advertisement * 0.20 + time_of_episode_without_advertisement
special_episodes_time = seasons * 10

total_time = (ceil(time_of_advertisement * episodes * seasons + special_episodes_time))

print(f"Total time needed to watch the {name_of_movie} series is {total_time} minutes.")
