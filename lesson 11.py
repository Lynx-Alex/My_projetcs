a = int(input())
b = int(input())
c = int(input())
d = reversed(sorted([a, b, c]))
if d[0] != d[1]:
    print(d[1] * 2 + 1)
else:
    print(a[1] * 2)