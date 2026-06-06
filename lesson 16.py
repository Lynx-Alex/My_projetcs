n = int(input())
c = input().split()
d = [int(i) for i in c]
a = d[0]
b = d[1]
if n > a and n > b:
    print((a + b) - n + 1)
elif n <= a and n <= b:
    print(n + 1)
else:
    print(min(a, b) + 1)