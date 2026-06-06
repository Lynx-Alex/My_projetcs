a = input()
if 10 <= len(a) <= 11:
    if len(a) == 11:
        a = a[1:]
    print("+7" + " (" + a[0:3] + ") " + a[3:6] + "-" + a[6:8] + "-" + a[8:])
else:
    print(a)