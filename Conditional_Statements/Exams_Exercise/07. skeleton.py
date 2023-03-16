minutes = int(input())
seconds = int(input())
length_meters = float(input())
seconds_for_100_meters = int(input())

control_time_in_seconds = minutes * 60 + seconds
cut_meters = length_meters / 120
cut_time = cut_meters * 2.5
time_of_marin = (length_meters / 100) * seconds_for_100_meters - cut_time

if time_of_marin <= control_time_in_seconds:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {time_of_marin:.3f}.")

else:
    print(f"No, Marin failed! He was {time_of_marin - control_time_in_seconds:.3f} second slower.")
