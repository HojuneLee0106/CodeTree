n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
grid=[[0 for _ in range(n)]for _ in range(n)]
for i in range(m):
    y=points[i][0]-1
    x=points[i][1]-1
    grid[y][x]=1
    c=0
    pos=0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for j in range(4):
        if y+dy[j]>=0 and x+dx[j]>=0 and y+dy[j]<n and x+dx[j]<n:
            if grid[y+dy[j]][x+dx[j]]==1:
                c+=1
                if c==3:
                    pos=1
        if c==4:
            pos=0
    print(pos)
# Please write your code here.