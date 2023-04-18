num = int(input())
counter = 0

for row in range(1, num + 1):
    for column in range(1, row + 1):
        counter += 1

        print(counter) if column == row else print(counter, end=" ")
        if counter == num:
            exit()
