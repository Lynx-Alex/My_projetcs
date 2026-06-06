a = int(input())
b = int(input())
count = 0
while b >= 1 and a != 0:
    count += 1
    b -= 2
    a -= 1
while a != 0 and a != 1:
    count += 1
    a -= 2
print(count, a, b)