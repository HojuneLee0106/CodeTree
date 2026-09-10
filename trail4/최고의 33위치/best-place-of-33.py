n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
total=0
for i in range(n-2):
    for j in range(n-2):
        answer=0
        for k in range(3):
            for l in range(3):
                if grid[i+k][j+l]==1:
                    answer+=1
        total=max(total,answer)
print(total)
# Please write your code here.
