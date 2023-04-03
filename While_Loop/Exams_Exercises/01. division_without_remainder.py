n = int(input())

p1 = 0
p2 = 0
p3 = 0
counter =0

for _ in range(n + 1):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

    counter += 1

    if counter == n:
        break

print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
