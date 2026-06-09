N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
stu=[0 for _ in range(N)]
answer=-1
for i in range(M):
    stu[student[i]-1]+=1
    if stu[student[i]-1]==K:
        answer=student[i]
        break
print(answer)
# Please write your code here.