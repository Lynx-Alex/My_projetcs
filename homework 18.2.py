n = int(input())
m = int(input())
a = (min(n, m) - 1) *  4
if m % 2 != 0 and n % 2 != 0 and n == m:
    print(2 * n - 5)
elif n == m:
    print((a - 4) // 2)
elif m % 2 != 0 and n % 2 != 0:
    print(a - 4)
elif m % 2 != 0 or n % 2 != 0:
    print(a - 2)
else:
    print(a)