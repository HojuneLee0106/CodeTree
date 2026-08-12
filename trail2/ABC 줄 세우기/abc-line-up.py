n = int(input())
arr = list(input().split())
answer=0
for i in range(n-1):
    for j in range(n-i-1):
        if ord(arr[j])>ord(arr[j+1]):
            t=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=t
            answer+=1
print(answer)
# Please write your code here.