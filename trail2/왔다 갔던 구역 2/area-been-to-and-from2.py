n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)
path=[0 for _ in range(10000)]
current=5000
for i in range(n):
    if dir[i]=="R":
        for j in range(current,current+x[i]):
            path[j]+=1
        current+=x[i]
    else:
        for j in range(current-1,current-x[i]-1,-1):
            path[j]+=1
        current-=x[i]
answer=0
for i in range(10000):
    if path[i]>1:
        answer+=1
print(answer)
# Please write your code here.