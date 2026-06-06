n = int(input())
a = int(input())
b = 0
while n > a:
    n -= n - a
    b += n - a
print(b)