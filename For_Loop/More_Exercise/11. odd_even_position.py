from sys import maxsize

num = int(input())

odd_sum = 0
even_sum = 0

even_max = - maxsize
even_min = maxsize
odd_max = - maxsize
odd_min = maxsize

for i in range(1, num + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f}," if odd_min != maxsize else "OddMin=No,")
print(f"OddMax={odd_max:.2f}," if odd_max != -maxsize else "OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f}," if even_min != maxsize else "EvenMin=No,")
print(f"EvenMax={even_max:.2f}" if even_max != -maxsize else "EvenMax=No")
