a1 = int(input())
a2 = int(input())
n = int(input())

letter_symbol = None

for symbol_1 in range(a1, a2):
    for symbol_2 in range(1, n):
        for symbol_3 in range(1, n // 2):
            if symbol_1 % 2 != 0:
                symbol_4 = symbol_1
                letter_symbol = chr(symbol_1)
                if (symbol_2 + symbol_3 + symbol_4) % 2 != 0:
                    print(f"{letter_symbol}-{symbol_2}{symbol_3}{symbol_4}")
