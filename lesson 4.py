summa = 0
quantity = 0
c = int(input())
while c != 0:
    summa += c
    if c % 10 == 0:
        quantity += 1
    c = int(input())
print(summa)
print(quantity)