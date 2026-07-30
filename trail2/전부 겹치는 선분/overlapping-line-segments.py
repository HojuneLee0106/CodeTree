N=int(input())
line=[]
big=0
for i in range(N):
    n=list(map(int, input().split()))
    b=max(n)
    big=max(big, b)
    line.append(n)
arr=[0 for _ in range(big+1)]
for i in range(N):
    for j in range(line[i][0], line[i][1]+1):
        arr[j]+=1
pos=False
for j in range(big+1):
    if arr[j]==N:
        pos=True
        break
if pos:
    print("Yes")
else:
    print("No")