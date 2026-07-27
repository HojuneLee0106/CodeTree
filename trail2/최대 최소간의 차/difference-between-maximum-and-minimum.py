N, K= map(int, input().split())
arr=list(map(int, input().split()))
min_n=min(arr)
max_n=max(arr)
answer=float('inf')
for i in range(max_n+1):
    new_arr=arr[:]
    d=0
    for j in range(N):
        low=i
        top=i+K
        if arr[j]>top:
            d+=(arr[j]-top)
        elif arr[j]<low:
            d+=(low-arr[j])
    answer=min(answer, d)
    
print(answer)
