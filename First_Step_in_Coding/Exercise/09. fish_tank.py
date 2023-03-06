length = int(input())
width = int(input())
height = int(input())
percent_filled = float(input()) / 100

volume_tank = length * width * height / 1000
volume = volume_tank - volume_tank * percent_filled

print(volume)
