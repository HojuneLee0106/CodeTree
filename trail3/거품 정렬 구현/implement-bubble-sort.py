n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            s=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=s
for i in range(n):
    print(arr[i], end=" ")
# Please write your code here.
