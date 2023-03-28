from math import ceil

h_wall = int(input())
w_wall = int(input())
no_paint_percent = int(input()) / 100

area_for_paint = h_wall * w_wall * 4
total_area_for_paint = ceil(area_for_paint - (area_for_paint * no_paint_percent))

while True:
    paint_litres = input()

    if paint_litres == "Tired!":
        print(f"{total_area_for_paint} quadratic m left.")
        break
    paint_litres = int(paint_litres)

    total_area_for_paint -= paint_litres

    if total_area_for_paint == 0:
        print("All walls are painted! Great job, Pesho!")
        break
        
    if total_area_for_paint < 0:
        print(f"All walls are painted and you have {abs(total_area_for_paint)} l paint left!")
        break
