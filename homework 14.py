m = int(input())
a = input().split()
b = [int(i) for i in a]
if m % 5 == m % 15:
    print(m + abs(m - 15) + b[2])
elif m % 5 == m % 10:
    print(m + abs(m - 10) + b[1])
else:
    print(m + abs(m - 5) + b[0])