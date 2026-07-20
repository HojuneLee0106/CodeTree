n, k = map(int, input().split())
arr = list(map(int, input().split()))
Inf=float('inf')
dp=[Inf]*n
dp[0]=arr[0]
for i in range(n):
    if dp[i]==Inf:
        continue
    for d in range(1,k+1):
        nxt=i+d
        if nxt<n:
            dp[nxt]=min(dp[nxt],max(dp[i],arr[nxt]))
print(dp[n-1])
# Please write your code here.