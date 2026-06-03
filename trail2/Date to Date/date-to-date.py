m1, d1, m2, d2 = map(int, input().split())
days=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer=0
if m1 == m2:
    answer = d2 - d1 + 1
else:
    for i in range(m1 + 1, m2):
        answer += days[i]
    answer += (days[m1] - d1 + 1)
    answer += d2
print(answer)


# Please write your code here.
