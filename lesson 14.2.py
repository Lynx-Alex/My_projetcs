n = int(input())
a = input().split()
([int(i) for i in a])
c = 0
d = 0
e = 1
for i in range(10):
    while d == e:
        c += 1
        d = a[c]
    e += 1
    print(d)
    print(i)