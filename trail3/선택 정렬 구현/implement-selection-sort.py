n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min=i
    for j in range(i,n):
        if arr[j]<arr[min]:
            min=j
    s=arr[i]
    arr[i]=arr[min]
    arr[min]=s
for i in range(n):
    print(arr[i],end=" ")

# Please write your code here.
