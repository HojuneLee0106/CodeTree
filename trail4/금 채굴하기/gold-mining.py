n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

golds=[(r,c) for r in range(n) for c in range(n) if grid[r][c]==1]
max_gold=0
for r in range(n):
    for c in range(n):
        dist_count=[0]*(2*n+1)
        for gr, gc in golds:
            dist=abs(r-gr)+abs(c-gc)
            dist_count[dist]+=1
        current_gold=0
        for k in range(2*n+1):
            current_gold+=dist_count[k]
            cost=k*k+(k+1)*(k+1)
            if current_gold*m>=cost:
                max_gold=max(max_gold,current_gold)
print(max_gold)
# Please write your code here.
