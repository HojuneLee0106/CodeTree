n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(i):
        if arr[i]<arr[j]:
            t=arr[j]
            arr[j]=arr[i]
            arr[i]=t
print(*arr)
# Please write your code here.
