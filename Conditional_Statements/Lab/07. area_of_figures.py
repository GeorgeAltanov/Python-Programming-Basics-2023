from math import pi

figure = input()
area = 0

if figure == "square":
    a = float(input())
    area = a * a

if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif figure == "circle":
    r = float(input())
    area = pi * r * r

elif figure == "triangle":
    b = float(input())
    h = float(input())
    area = b * h / 2

print(f"{area:.3f}")
