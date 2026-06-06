size = int(input())
small = 3
summ = 0
while small <= size:
    summ += (small - 1) * 4
    small += 4
print(summ)