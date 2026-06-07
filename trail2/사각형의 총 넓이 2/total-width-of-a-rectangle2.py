n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
coor=[[0 for _ in range(200)]for _ in range(200)]
zero=100
for i in range(n):
    for j in range(zero+x1[i],zero+x2[i]):
        for k in range(zero+y1[i],zero+y2[i]):
            if coor[k][j]==0:
                coor[k][j]=1
answer=0
for i in range(200):
    for j in range(200):
        if coor[i][j]==1:
            answer+=1
print(answer)
# Please write your code here.