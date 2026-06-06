from lesson_12 import
first = translate_split(first)
a = first[0] ** 2
n = first[1]
distance = 0
a_now = a
for i in range(n + 1):
    a_now = a * i
    distance += a_now
    second = translate_split(second)
    d = second[0]
    v = second[1]
    oil = d - distance
    if a_now > oil:
        a_now -= oil
    else:
        print(distance + a_now)
    a_now += (a - a_now) ** 0.5 // 1 ** 2
    distance = d
print(distance)