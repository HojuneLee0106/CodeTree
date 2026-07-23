N = int(input())
heights = [int(input()) for _ in range(N)]
min_cost=float('inf')
max_h=max(heights)
for i in range(max_h+1):
    current_cost=0
    for h in heights:
        if h<i:
            current_cost+=(i-h)**2
        elif h>i+17:
            current_cost+=(h-(i+17))**2
    if current_cost<min_cost:
        min_cost=current_cost
print(min_cost)
# Please write your code here.