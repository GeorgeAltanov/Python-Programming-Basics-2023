first_num, second_num, third_num = int(input()), int(input()), int(input())

second_num_prime = 0
non_num_prime = 0

for num_1 in range(1, first_num + 1):

    for num_2 in range(2, second_num + 1):
        condition = True
        for number in range(2, num_2):
            if num_2 % number == 0:
                condition = False
        if not condition:
            continue
        else:
            second_num_prime = num_2

        for num_3 in range(1, third_num + 1):

            if num_1 % 2 == 0 and num_3 % 2 == 0:
                print(f"{num_1} {second_num_prime} {num_3}")
