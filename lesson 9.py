n = int(input())
x = input()
y = input()
a = 0
num = (x+y)
for i in range(1, n+1):
    for j in str(i):
        if j not in num:
            break
    else:
        a += 1
print(a)