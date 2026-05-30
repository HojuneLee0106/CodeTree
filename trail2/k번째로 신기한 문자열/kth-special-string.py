n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
answer=[]
for i in str:
    if i.startswith(t):
        answer.append(i)
answer.sort()
print(answer[k-1])
# Please write your code here.