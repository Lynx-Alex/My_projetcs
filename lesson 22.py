a = int(input()) # оба белых
b = int(input()) # на правой белая
c = int(input()) # на правой черная
d = int(input()) # оба черных
if b == 0 and c == 0:
    print(max(a, d))
elif b > c:
    print(2 * c + 1 + a + d)
elif c > b:
    print(2 * b + 1 + a + d)
elif b == c:
    print(2 * c + a + d)