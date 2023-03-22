num = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(num):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / num * 100:.2f}%\n{p2 / num * 100:.2f}%\n"
      f"{p3 / num * 100:.2f}%\n{p4 / num * 100:.2f}%\n{p5 / num * 100:.2f}%")
