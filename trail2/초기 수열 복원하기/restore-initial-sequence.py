n = int(input())
adjacent = list(map(int, input().split()))
c=[0 for _ in range(n)]
for i in range(1,n+1):
    arr=[0]*n
    arr[0]=i
    is_valid=True
    for j in range(1,n):
        arr[j]=adjacent[j-1]-arr[j-1]
        if arr[j]<1 or arr[j]>n:
            is_valid=False
            break
    if is_valid and len(set(arr))==n:
        print(*arr)
        break
# Please write your code here.