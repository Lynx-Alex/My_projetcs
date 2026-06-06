a = [int(i) for i in input().split()]
a_max = (sum(a) + 100 * len(a)) * 0.4
n = int(input())
result = 0
c = 0
for i in range(n):
    b = [int(i) for i in input().split()]
    c = 0
    for i in range(len(a)):
        if a[i] == b[i + 1]:
            c += b[i + 1] + 100
        else:
            c += b[i + 1]
    if c >= a_max:
        result += 1
print(result)