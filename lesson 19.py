n = int(input())
m = int(input())
a = (min(n, m) - 1) *  4
if n % 2 != 0  and n / 2 <= m:
    a -= 2
if m % 2 != 0 and m / 2 <= n:
    a -= 2
if n == m:
    a -= 4
    a = a // 2
print(a)