N, S = map(int, input().split())
arr = list(map(int, input().split()))
min_score=[]
sum_score=sum(arr)
for i in range(N-1):
    for j in range(i+1,N):
        min_score.append(abs(S-sum_score+arr[i]+arr[j]))
print(min(min_score))
# Please write your code here.