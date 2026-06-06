def translate_split():
    return [int(i) for i in input().split()]
first = translate_split()
a = first[0] ** 2
n = first[1]
distance = 0
a_now = a
for e in range(n + 1):
    second = translate_split()
    d = second[0]
    v = second[1]
    oil = d - distance
    if a_now >= oil:
        a_now -= oil
    else:
        break
    a_now += (((a - a_now) if (a - a_now) < v else v) ** 0.5 // 1) ** 2
    distance = d
print(int (distance + a_now))