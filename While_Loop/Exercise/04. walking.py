STEPS = 10_000
steps_counter = 0

while steps_counter < STEPS:
    steps = input()
    if steps == "Going home":
        steps_counter += int(input())  # добавя следващите стъпки и тогава спира
        break

    steps_counter += int(steps)

if steps_counter >= STEPS:
    print("Goal reached! Good job!")
    print(f"{steps_counter - STEPS} steps over the goal!")

else:
    print(f"{STEPS - steps_counter} more steps to reach goal.")
