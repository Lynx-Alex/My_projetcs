n = int(input())
x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
xo = a[0]
d = a[1]
m = int(input())
for i in range(m):
    t = int(input())
if abs(d - x[0]) <= abs(d - x[-1]):