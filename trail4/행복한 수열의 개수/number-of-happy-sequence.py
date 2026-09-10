n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=0
for i in range(n):
    current=0
    c=0
    for j in range(n):
        if grid[i][j]==current:
            c+=1
            if c>=m:
                answer+=1
                break
        else:
            current=grid[i][j]
            c=1
            if c>=m:
                answer+=1
                break
for i in range(n):
    current=0
    c=0
    for j in range(n):
        if grid[j][i]==current:
            c+=1
            if c>=m:
                answer+=1
                break
        else:
            current=grid[j][i]
            c=1
            if c>=m:
                answer+=1
                break
print(answer)
# Please write your code here.
