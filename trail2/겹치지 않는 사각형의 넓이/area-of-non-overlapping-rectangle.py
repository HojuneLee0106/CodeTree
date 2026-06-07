x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())
coor=[[0 for _ in range(2000)] for _ in range(2000)]
zero=1000
for i in range(2):
    for j in range(zero+x1[i],zero+x2[i]):
        for k in range(zero+y1[i],zero+y2[i]):
            if coor[k][j]==0:
                coor[k][j]=1
for j in range(zero+x1[2],zero+x2[2]):
        for k in range(zero+y1[2],zero+y2[2]):
            if coor[k][j]==1:
                coor[k][j]=0
answer=0
for i in range(2000):
    for j in range(2000):
        if coor[i][j]==1:
            answer+=1
print(answer)
# Please write your code here.