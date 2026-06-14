n, m = map(int, input().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
grid=[[0 for _ in range(m)]for _ in range(n)]
x=0
y=0
num=1
curr=0
for i in range(n):
    for j in range(m):
        grid[y][x]=num
        num+=1
        nx=x+dx[curr]
        ny=y+dy[curr]
        if nx<0 or ny<0 or nx>=m or ny>=n or grid[ny][nx]!=0:
            curr+=1
            curr%=4
            x+=dx[curr]
            y+=dy[curr]
        else:
            x+=dx[curr]
            y+=dy[curr]
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()
# Please write your code here.