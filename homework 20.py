n = int(input())
d = []
m_length = 0
m_num = 0
for i in range(n):
    d.append(int(input()))
for i in range(n):
    summ = 0
    summ += d[i]
    if n > 2 * i:
        summ += d[2 * i]
    if n > 2 * i + 1:
        summ += 2 * d[2 * i + 1]
    if n > 2 * i + 2:
        summ += d[2 * i + 2]
    if summ > m_num:
        m_num = summ
        m_length = i + 1
print(m_num)
print(m_length)