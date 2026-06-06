a = input().split()
b = [int(i) for i in a]
t = b[0]
n = b[1]
c = []
A = 0
d = []
e = 0
for i in range(t):
    c.append(int(input()))
for i in range(t):
    A += 2 ** c[i]
result = (2 ** n - 1) - A
while result >= 1:
    if result % 2 == 1:
        print(e, end=" ")
    result = result // 2
    e += 1
print(1, 2, 3, sep = " штук, ")