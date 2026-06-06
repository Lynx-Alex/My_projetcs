a = int(input())
b = int(input())
while a >= (10 ** b):
    a //= 10
print(a % 10)