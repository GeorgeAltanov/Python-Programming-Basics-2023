n = int(input())

for a in range(1, 10):
    for b in range(9, a -1, -1):
        for c in range(1, 10):
            for d in range(9, c - 1, -1):

                if (a * b * c * d) // (a + b + c + d)  == 3 and n % 3 == 0:
                    print(d,c,b,a)
                    exit()

                elif a + b + c + d == a * b * c * d and n % 10 == 5:
                    print(a,b,c,d)
                    exit()

else:
    print("Nothing found")
    exit()
