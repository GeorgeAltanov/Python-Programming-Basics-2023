num_1 = input()
num_2 = input()

for first_num in range(int(num_1[0]), int(num_2[0]) + 1):
    for second_num in range(int(num_1[1]), int(num_2[1]) + 1):
        for third_num in range(int(num_1[2]), int(num_2[2]) + 1):
            for fourth_num in range(int(num_1[3]), int(num_2[3]) + 1):
                if first_num % 2 != 0 and second_num % 2 != 0 and third_num % 2 != 0 and fourth_num % 2 != 0:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
