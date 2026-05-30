n = int(input())
arr = list(map(int, input().split()))
answer=[]
x=0
for i in range(n):
    if i%2!=1:
        answer.append(arr[i])
        answer.sort()
        print(answer[x],end=" ")
        x+=1
    else:
        answer.append(arr[i])
# Please write your code here.