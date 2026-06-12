n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
curr=0
i=0
j=0
for x in range(1, n*m+1):
    arr[i][j]=x
    ny=i+dy[curr]
    nx=j+dx[curr]
    if 0<=nx<=m-1 and 0<=ny<=n-1 and arr[ny][nx]==0:
        i+=dy[curr]
        j+=dx[curr]
    else:
        curr+=1
        curr%=4
        i+=dy[curr]
        j+=dx[curr]
for h in range(n):
    for k in range(m):
        print(arr[h][k], end=" ")
    print()
# Please write your code here.