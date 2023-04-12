start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for num_1 in range(start_interval, final_interval + 1):
    for num_2 in range(start_interval, final_interval + 1):
        combination_counter += 1
        combination_sum = num_1 + num_2

        if combination_sum == magic_number:
            break_condition = True
            print(f"Combination N:{combination_counter} ({num_1} + {num_2} = {magic_number})")
            break          

    if break_condition:
        break             

if not break_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
