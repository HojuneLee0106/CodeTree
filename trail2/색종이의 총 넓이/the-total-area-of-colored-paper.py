n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
coor=[[0 for i in range(200)]for j in range(200)]
start=100
for i in range(n):
    for j in range(start+x[i],start+x[i]+8):
        for k in range(start+y[i], start+y[i]+8):
            if coor[k][j]==0:
                coor[k][j]=1
answer=0
for i in range(200):
    for j in range(200):
        if coor[i][j]==1:
            answer+=1
print(answer)
# Please write your code here.