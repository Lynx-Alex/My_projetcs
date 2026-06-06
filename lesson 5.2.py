a = int(input())
b = 0
c = 1
d = 1
while a != b:
    b += 1
    sum = c + d
    c = d
    d = sum
    print(c)