open_tabs = int(input())
salary = float(input())

FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

for _ in range(open_tabs):
    link = input()
    if link == "Facebook":
        salary -= FACEBOOK
    elif link == "Instagram":
        salary -= INSTAGRAM
    elif link == "Reddit":
        salary -= REDDIT

    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(f"{int(salary)}")
