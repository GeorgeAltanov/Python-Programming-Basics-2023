length = float(input()) * 100
width = float(input()) * 100

working_spaces_on_rows = (width - 100) // 70
working_spaces_on_cols = length // 120

all_spaces = int((working_spaces_on_cols * working_spaces_on_rows) - 3)

print(all_spaces)
