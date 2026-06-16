N = int(input())
A = list(map(int, input().split()))
answer=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if A[i]<=A[j]<=A[k]:
                answer+=1
print(answer)
# Please write your code here.