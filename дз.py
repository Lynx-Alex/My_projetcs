a = int(input())
if a >= 0:
    print("положительное")
else:
    print("отрицательное")
b = a / 2
if b == int(b):
    print("четное")
else:
    print("нечетное")
if a % 2 == 0:
    print("четное")
else:
    print("нечетное")
c = a % 10
if c == 2:
    print("заканчивается на 2")
else:
    print("не заканчивается на 2")