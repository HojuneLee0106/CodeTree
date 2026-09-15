n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=0
for i in range(n-1):
    for j in range(m-1):
        mi=float("inf")
        h=0
        for k in range(2):
            for l in range(2):
                mi=min(mi,grid[i+k][j+l])
                h+=grid[i+k][j+l]
        answer=max(answer,h-mi)
for i in range(n):
    for j in range(m-2):
        h=0
        for k in range(3):
            h+=grid[i][j+k]
        answer=max(answer,h)
for i in range(m):
    for j in range(n-2):
        h=0
        for k in range(3):
            h+=grid[j+k][i]
        answer=max(answer,h)
print(answer)

# Please write your code here.
