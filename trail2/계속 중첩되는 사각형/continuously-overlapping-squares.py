n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
coor=[[0 for _ in range(200)]for _ in range(200)]
start=100
for i in range(n):
    if i%2==0:
        for j in range(start+x1[i], start+x2[i]):
            for k in range(start+y1[i], start+y2[i]):
                coor[k][j]=1
    else:
        for j in range(start+x1[i], start+x2[i]):
            for k in range(start+y1[i], start+y2[i]):
                coor[k][j]=2
answer=0
for i in range(200):
    for j in range(200):
        if coor[i][j]==2:
            answer+=1
print(answer)
# Please write your code here.