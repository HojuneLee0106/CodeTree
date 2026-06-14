n, m = map(int, input().split())
E=["A","B","C","D",'E',"F",'G',"H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z']
num=0
grid=[[0 for _ in range(m)]for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
x=0
y=0
curr=0
for i in range(n):
    for j in range(m):
        grid[y][x]=E[num]
        num+=1
        num%=26
        nx=x+dx[curr]
        ny=y+dy[curr]
        if nx<0 or ny<0 or nx>=m or ny>=n or grid[ny][nx]!=0:
            curr+=1
            curr%=4
            x+=dx[curr]
            y+=dy[curr]
        else:
            x=nx
            y=ny
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()
# Please write your code here.
