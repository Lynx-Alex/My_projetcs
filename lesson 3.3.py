from random import randint
b = int(input())
number = randint(1, b)
a = int(input("введите число "))
while a != number:
    print("неверно")
    if a < number:
        print("больше")
    elif a > number:
        print("меньше")
    a = int(input("введите число "))
print("верно")