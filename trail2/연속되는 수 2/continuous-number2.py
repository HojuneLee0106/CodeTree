n = int(input())
arr = [int(input()) for _ in range(n)]
curr=arr[0]
answer=[]
c=0
for i in range(len(arr)):
    if i==len(arr)-1:
        if curr==arr[i]:
            c+=1
            answer.append(c)
        else:
            answer.append(c)
            answer.append(1)
    elif i==0:
        curr=arr[i]
        c+=1
    elif curr != arr[i]:
        answer.append(c)
        c=1
        curr=arr[i]
    else:
        c+=1
print(max(answer))
# Please write your code here.