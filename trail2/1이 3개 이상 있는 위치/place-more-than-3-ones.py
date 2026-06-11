n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
answer=0
for i in range(n):
    for j in range(n):
        c=0
        for x,y in zip(dx,dy):
            if i+y>n-1 or i+y<0 or j+x>n-1 or j+x<0:
                continue
            else:
                if grid[i+y][j+x]==1:
                    c+=1
                if c>=3:
                    answer+=1
                    break
print(answer)
# Please write your code here.