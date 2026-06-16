R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
answer=0
x, y=0, 0
queue=[]
queue.append((0,0,0))
while queue:
    y,x,c=queue.pop()
    if y==R-1 and x==C-1:
        if c==3:
            answer+=1
        continue
    if c>=3:
        continue
    current_color=grid[y][x]
    for i in range(y+1,R):
        for j in range(x+1,C):
            if grid[i][j]!=current_color:
                queue.append((i, j, c + 1))
print(answer)
# Please write your code here.