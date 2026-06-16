n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=[]
for i in range(n):
    for j in range(n-2):
        coin=0
        for k in range(j,j+3):
            if grid[i][k]==1:
                coin+=1
        answer.append(coin)
print(max(answer))
# Please write your code here.