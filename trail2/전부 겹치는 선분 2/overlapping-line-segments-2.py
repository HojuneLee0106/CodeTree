n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]
pos=False
for i in range(n):
    arr=[0 for _ in range(101)]
    for j in range(n):
        if i==j:
            continue
        for k in range(x1[j],x2[j]+1):
            arr[k]+=1
    if max(arr)==n-1:
        pos=True
        break
if pos:
    print("Yes")
else:
    print("No")        
# Please write your code here.