from math import floor

processors_count = int(input())
employers = int(input())
workdays = int(input())

PRICE_PER_PROCESSOR = 110.10

work_hours = employers * workdays * 8
made_processors = floor(work_hours / 3)

if made_processors >= processors_count:
    print(f"Profit: -> {(made_processors - processors_count) * PRICE_PER_PROCESSOR:.2F} BGN")

else:
    print(f"Losses: -> {(processors_count - made_processors) * PRICE_PER_PROCESSOR:.2F} BGN")
