from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
swim_a_distance_of_1_m_in_seconds = float(input())

delay = floor(distance_in_meters / 15) * 12.5
total_time_of_ivan = distance_in_meters * swim_a_distance_of_1_m_in_seconds + delay

if total_time_of_ivan < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_of_ivan:.2f} seconds.")
    
else:
    print(f"No, he failed! He was {total_time_of_ivan - record_in_seconds:.2f} seconds slower.")
