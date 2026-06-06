n = int(input())
import time
start_time = time.time()
a = []
for i in range(2, n+1):
    a.append(i)
p = 2
while p * p < n:
    if p in a:
        for i in range(2 * p, n + 1, p):
            try:
                a.remove(i)
            except:
                pass
    p += 1
print(a)
print("___ %s seconds ___" % (time.time() - start_time))