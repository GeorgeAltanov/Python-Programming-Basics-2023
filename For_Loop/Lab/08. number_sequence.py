import sys

num = int(input())

MAX_NUMBER = -sys.maxsize
MIN_NUMBER = sys.maxsize

for _ in range(num):
    number = int(input())
    if number > MAX_NUMBER:
        MAX_NUMBER = number
    if number < MIN_NUMBER:
        MIN_NUMBER = number

print(f"Max number: {MAX_NUMBER}")
print(f"Min number: {MIN_NUMBER}")
