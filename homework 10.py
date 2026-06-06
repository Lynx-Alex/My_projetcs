a = int(input())
b = int(input())
c = int(input())
if a > c and b > c:
    if a > b:
        print(a)
    if b > a:
        print(b)
elif c > a and b > a:
    if c > b:
        print(c)
    if b > c:
        print(b)
elif a > b and c > b:
    if c > a:
        print(c)
    if a > c:
        print(a)