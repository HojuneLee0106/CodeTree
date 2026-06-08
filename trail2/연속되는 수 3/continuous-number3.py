N = int(input())
arr = [int(input()) for _ in range(N)]
c=1
curr=1
answer=[]
for i in range(N):
    if i==len(arr)-1:
        if arr[i]<0 and curr<0:
            c+=1
            answer.append(c)
        elif arr[i]>0 and curr>0:
            c+=1
            answer.append(c)
        else:
            answer.append(c)
            answer.append(1)
    elif i==0:
        if arr[i]>0:
            curr=1
        else:
            curr=-1
    elif arr[i]>0 and curr>0:
        c+=1
    elif arr[i]<0 and curr<0:
        c+=1
    else:
        if curr>0:
            answer.append(c)
            c=1
            curr=-1
        else:
            answer.append(c)
            c=1
            curr=1
print(max(answer))
# Please write your code here.