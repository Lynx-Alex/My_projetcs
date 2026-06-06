d = int(input())
m = int(input())
y = int(input())
d2 = int(input())
m2 = int(input())
y2 = int(input())
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
a = 0
for j in range(m - 1):
    a += l[j]
a += d
b = 0
for g in range(m2 - 1):
    b += l[g]
b += d2
all = 0
for i in range(n):
    all += l[i]
print(all * (y2 - y) - a + b + 1)