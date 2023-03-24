hours = 0
minutes = 0

while True:
    if minutes > 59:
        hours += 1
        minutes = 0
        if hours > 23:
            break
    print(f"{hours} : {minutes}")
    minutes += 1
