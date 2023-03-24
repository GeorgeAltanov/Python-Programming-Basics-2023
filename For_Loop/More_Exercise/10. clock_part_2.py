hours = 0
minutes = 0
seconds = 0

while True:
    if seconds > 59:
        minutes += 1
        seconds = 0
        if minutes > 59:
            hours += 1
            minutes = 0
        if hours > 23:
            break
    print(f"{hours} : {minutes} : {seconds}")
    seconds += 1
