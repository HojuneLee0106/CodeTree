n = int(input())
grid = [[0] * n for _ in range(n)]
x=n//2
y=n//2
num=2
grid[y][x]=1
dx=[1,0,-1,0]
dy=[0,-1,0,1]
curr=0
change=0
move_len=1
while num<n*n:
    for _ in range(2):
        for _ in range(move_len):
            if num>n*n:
                break
            x+=dx[curr]
            y+=dy[curr]
            grid[y][x]=num
            num+=1
        curr+=1
        curr%=4
    move_len+=1
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
# Please write your code here.
