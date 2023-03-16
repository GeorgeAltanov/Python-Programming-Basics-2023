time_for_movie = int(input())
scenes = int(input())
time_of_scenes = int(input())

preparation = time_for_movie * 0.15
needed_time_for_scenes = scenes * time_of_scenes
time_needed = preparation + needed_time_for_scenes

if time_needed < time_for_movie:
    print(f"You managed to finish the movie on time! You have {round(time_for_movie - time_needed)} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {round(time_needed - time_for_movie)} minutes.")
