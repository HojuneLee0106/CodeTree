n = int(input())
arr = [int(input()) for _ in range(n)]
c=1
curr=1001
answer=[]
for i in range(n):
    if i==len(arr)-1:
        if arr[i]>curr:
            c+=1
            answer.append(c)
        else:
            answer.append(c)
            answer.append(1)
    elif i==0:
        curr=arr[i]
    elif arr[i]>curr:
        c+=1
        curr=arr[i]
    else:
        answer.append(c)
        c=1
        curr=arr[i]
print(max(answer))
# Please write your code here.