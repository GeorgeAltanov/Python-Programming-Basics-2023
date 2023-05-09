climbed_meters = 5364
days = 1

while climbed_meters < 8848:
    sleep = input()

    if sleep == "END" or days > 5:
        break

    meters = int(input())

    if sleep == "Yes":
        days += 1
    elif sleep == "No":
        days = days

    climbed_meters += meters

if climbed_meters >= 8848:
    print(f"Goal reached for {days} days!")

else:
    print(f"Failed!")
    print(f"{climbed_meters}")
