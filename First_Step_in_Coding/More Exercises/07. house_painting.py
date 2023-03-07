x = float(input())
y = float(input())
h = float(input())

GREEN_PAINT = 3.4
RED_PAINT = 4.3

doors = 1.2 * 2
windows = 1.5 * 1.5 * 2

front_and_back_walls = (x * x * 2) - doors
side_walls = (x * y * 2) - windows
total_green_paint = (front_and_back_walls + side_walls) / GREEN_PAINT

front_and_back_roof = (x * h / 2) * 2
side_roof = x * y * 2
total_red_paint = (front_and_back_roof + side_roof) / RED_PAINT

print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")
