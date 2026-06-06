import math
n = int(input())
k = int(input())
b = 0
for i in range(k):
    a = [int(j) for j in input().split()]
    b += n // (2 ** i) * a[0]
print(b)