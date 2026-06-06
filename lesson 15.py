import math
m = int(input())
a = input().split()
b = [int(i) for i in a]
t = [15, 10, 5]
s = []
for i in range(len(t)):
    s.append(math.ceil(m / t[i]) * t[i] - m + b[i])
print(min(s))