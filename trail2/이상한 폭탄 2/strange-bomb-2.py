N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
answer=[]
for i in range(N):
    for j in range(i+1,i+K+1):
        if j>=N:
            break
        if num[i]==num[j]:
            answer.append(num[i])
            break
if len(answer)==0:
    print(-1)
else:
    print(max(answer))
# Please write your code here.