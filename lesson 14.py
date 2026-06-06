k = int(input())
d = k ** 0.5
areas = set()
answers = set()
for a in range(int(d + 1)):
#    for g in range(int(d +1)):
#        if i ** 2 + g ** 2 == k:
#            print(i * g / 2)
    b = (k - a ** 2) ** 0.5
    if int(b) == b:
        b = int(b)
        areas.add(a * b / 2)
for a in areas:
    for b in areas:
        answers.add(int(a + b))
ans_list = list(answers)

print(len(sorted(ans_list)))
for i in sorted(ans_list):
    print(i)