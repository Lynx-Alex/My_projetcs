n = int(input())
x = int(input())
y = int(input())
if (x * 10 + y) <= n and (x * 10 + y) != 0 + y:
    print(x * 10 + y)

if (y * 10 + x) <= n and (y * 10 + x) != 0 + x:
    print(y * 10 + x)

if x <= n:
    print(x)

if y <= n and y != 0:
    print(y)

if (x * 10 + x) <= n and (x * 10 + x) != 0:
    print(x * 10 + x)

if (y * 10 + y) <= n and (y * 10 + y) != 0:
    print(y * 10 + y)