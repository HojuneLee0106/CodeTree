x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
coor=[[0 for _ in range(2000)] for _ in range(2000)]
start=1000
for j in range(start+x1[0],start+x2[0]):
        for k in range(start+y1[0],start+y2[0]):
            if coor[k][j]==0:
                coor[k][j]=1
for j in range(start+x1[1],start+x2[1]):
        for k in range(start+y1[1],start+y2[1]):
            if coor[k][j]==1:
                coor[k][j]=0
co_x=[]
co_y=[]
for i in range(2000):
    for j in range(2000):
        if coor[i][j]==1:
            co_x.append(i)
            co_y.append(j)
if len(co_x)==0 or len(co_y)==0:
    print(0)
else:
    answer = (max(co_x) - min(co_x) + 1) * (max(co_y) - min(co_y) + 1)
    print(answer)
# Please write your code here.