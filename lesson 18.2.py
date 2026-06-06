a = int(input())
b = int(input())
n = int(input())
m = int(input())
min_t = (a + 1) * (n - 1) + 1
max_t = (a + 1) * (n - 1) + 1 + 2 * a
min_t2 = (b + 1) * (m - 1) + 1
max_t2 = (b + 1) * (m - 1) + 1 + 2 * b
if max(min_t, min_t2) > min(max_t, max_t2):
    print(-1)
else:
    if min_t > min_t2:
        print(min_t)
    else:
        print(min_t2)
    if max_t < max_t2:
        print(max_t)
    else:
        print(max_t2)
print()